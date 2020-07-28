from transformers import pipeline
import logging
from transformers import AutoTokenizer
from transformers import AutoModelWithLMHead
from transformers import NerPipeline

# https://sites.google.com/site/germeval2014ner/data
# https://huggingface.co/bert-base-german-cased
# TODO: Kryptische Lables auflösen. Ergebnis schlecht
#  Aulösung hier: https://s3.amazonaws.com/models.huggingface.co/bert/dbmdz/bert-large-cased-finetuned-conll03-english/config.json

# Das ganze Fine-Tuning geht verloren


nlp = pipeline(task="ner", model="bert-base-german-cased")

print(nlp("Wir fahren nach Braunschweig"))