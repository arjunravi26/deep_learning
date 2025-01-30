from transformers import BertTokenizer
from transformers import AutoTokenizer

bert_tokenizer = BertTokenizer.from_pretrained("bert-base-cased")
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
