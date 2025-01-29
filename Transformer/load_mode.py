from transformers import AutoModelForSequenceClassification, AutoTokenizer

checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"

# Load the model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained(checkpoint)
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

model.to("cuda")
# Save it locally
model.save_pretrained("./local_model")
tokenizer.save_pretrained("./local_model")
