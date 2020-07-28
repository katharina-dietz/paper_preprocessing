from transformers import BertTokenizer
from transformers import pipeline
import logging

# Log for more details on what is happening hiere
logging.basicConfig(level=logging.INFO)

# load pretrained model tokenizer (vocabulary)
tokenizer = BertTokenizer.from_pretrained("bert-base-multilingual-cased")

with open("../data_in/rieger.txt", encoding="utf-8") as file:
    text = file.read()

print(text)

tokenized_text = tokenizer.tokenize(text)
print(tokenized_text)

# Convert token to vocabulary instances
indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)

nlp = pipeline("ner")
print("NLP Text_tokenized")
# for i in range(len(text)):
#   print(nlp(text[i]))

my_list_2 = nlp(tokenized_text)
print(my_list_2)


file2 = open("output2.csv", "w", encoding="utf-8")
for i in range(len(my_list_2)):
    file2.write(str(my_list_2[i]))
    file2.write("\n")

