from transformers import BertTokenizer
from transformers import AutoTokenizer

bert_tokenizer = BertTokenizer.from_pretrained("bert-base-cased")
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
tokens = tokenizer("Using a Transformer network is simple")
print(tokens)

# load model that saved on local disk
# tokenizer.save_pretrained("directory_on_my_computer")
