from transformers import BertTokenizer
from transformers import pipeline
import logging
import csv

from transformers import AutoTokenizer
from transformers import modeling_auto

# Log for more details on what is happening hiere
logging.basicConfig(level=logging.INFO)
with open("../data_in/rieger.txt", encoding="utf-8") as file:
    text = file.read()

nlp = pipeline("ner")
print(nlp(text))


