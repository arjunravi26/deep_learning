import pickle

import numpy as np
import pandas as pd
import streamlit as st
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler

loaded_model = tf.keras.models.load_model('model.h5')
with open('label_encoder_gender.pkl', 'rb') as file:
    label_encoder_gender = pickle.load(file)

with open('onehot_encoder_geography.pkl', 'rb') as file:
    onehot_geo = pickle.load(file)

with open('scale.pkl', 'rb') as file:
    scaler = pickle.load(file)

st.title("Customer Chrun Prediction")
geography = st.selectbox("Geography",onehot_geo.categories_[0])
gender = st.selectbox('Gender',label_encoder_gender.classes_)
age = st.slider('Age',18,92)
balance = st.number_input('Balance')
credit_scores = st.number_input('Credit Score')
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider('Tenure',0,10)
num_of_products = st.slider('Number of Products',1,4)
has_cr_card = st.selectbox('Has Credit Card',[0,1])
is_active_member = st.selectbox('Is Active Member',[0,1])
geo_encoded = onehot_geo.transform([[geography]])
geo_encoded_df = pd.DataFrame(geo_encoded,columns=onehot_geo.get_feature_names_out())
input_data = {
    'CreditScore':[credit_scores],
    'Geography': ['France'],
    'Gender':[gender],
    'Age':[age],
    'Tenure':[tenure],
    'Balance':[balance],
    'NumOfProducts':[num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember':[is_active_member],
    'EstimatedSalary':[estimated_salary]
}
input_df = pd.DataFrame(input_data)
input_df['Gender'] = label_encoder_gender.transform(input_df['Gender'])
input_data = pd.concat([input_df.reset_index(drop=True),geo_encoded_df],axis=1)
input_data.drop('Geography',axis=1,inplace=True)
df_scaled = scaler.transform(input_data)
prediction_prob = loaded_model.predict(df_scaled)
st.write(f"Predicted probability is {prediction_prob}")
if prediction_prob > 0.5:
   st.write('The Customer is likely to churn')
else:
   st.write('The Customer is not likely to churn')