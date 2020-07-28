from transformers import BertTokenizer
from transformers import pipeline
import logging

from transformers import AutoTokenizer
from transformers import modeling_auto

# Log for more details on what is happening hiere
logging.basicConfig(level=logging.INFO)

# load pretrained model tokenizer (vocabulary)
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Tokenize input
text = "[CLS] Who was Jim Henson ? [SEP] Jim Henson was a puppeteer [SEP]"
tokenized_text = tokenizer.tokenize(text)
print(tokenized_text)

# Convert token to vocabulary instances
indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
print(indexed_tokens)

nlp = pipeline("sentiment-analysis")
print(nlp("I hate you"))
print(nlp("I love you"))
