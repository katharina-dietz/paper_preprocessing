from transformers import BertTokenizer
from transformers import pipeline
import logging

from transformers import AutoTokenizer
from transformers import modeling_auto

# Log for more details on what is happening hiere
logging.basicConfig(level=logging.INFO)


nlp = pipeline("ner")
print(nlp("J'aime mon ordinateur du Apple"))

