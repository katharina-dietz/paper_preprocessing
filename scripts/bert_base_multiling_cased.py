from transformers import BertTokenizer
from transformers import pipeline
import logging

from transformers import AutoTokenizer
from transformers import modeling_auto

# Log for more details on what is happening hiere
logging.basicConfig(level=logging.INFO)

# load pretrained model tokenizer (vocabulary)
tokenizer = BertTokenizer.from_pretrained("bert-base-multilingual-cased")

# Tokenize input
text = "[CLS] Who was Jim Henson ? [SEP] Jim Henson was a puppeteer [SEP]"
tokenized_text = tokenizer.tokenize(text)
print(tokenized_text)

# Convert token to vocabulary instances
indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
print(indexed_tokens)

nlp = pipeline("ner")
mein_text = "Wir fahren nach Braunschweig. Wir wissen noch nicht was wir dort machen. Vielleicht treffen wir Ludwig oder den Papst. Das wird lustig. Enid Blyton kommt auch."
print(nlp(mein_text))

tokenized_text = tokenizer.tokenize(mein_text)
analyse_from_token =  nlp(tokenized_text)
print("analyse from token")
print(analyse_from_token)
meine_liste = nlp(mein_text)
print(meine_liste)
print(meine_liste[0])

for i in range(5):
    print(meine_liste[i])

for i in range(len(meine_liste)):
    print(meine_liste[i])

#### TODO hier jetzt in File schreiben

file = open("bert_kurz.txt", "w")

for i in range(len(meine_liste)):
    file.write(str(meine_liste[i]))

