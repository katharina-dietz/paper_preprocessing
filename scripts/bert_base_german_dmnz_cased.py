from transformers import pipeline
import logging
from transformers import AutoTokenizer
from transformers import AutoModelWithLMHead
from transformers import NerPipeline

# https://huggingface.co/dbmdz/bert-base-german-cased

logging.basicConfig(level=logging.INFO)

nlp = pipeline(task="ner", model="bert-base-german-cased")

print(nlp("Wir fahren nach Braunschweig"))