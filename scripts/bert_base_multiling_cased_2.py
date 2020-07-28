from transformers import BertTokenizer
from transformers import pipeline
import logging
from csv import DictWriter
from transformers import AutoTokenizer
from transformers import modeling_auto
import csv

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

with open("../data_in/rieger.txt", encoding="utf-8") as file:
    text = file.read()


nlp = pipeline("ner")
print(nlp("Niemand anderer als Jean-Jacques Rousseau - jener Aufklärer, der als einer der schärfsten Kritiker der “philosophes” à la Voltaire zu gelten hat und der früh die Widersprüche der bürgerlichen Aufklärung offenlegte - gibt zu Beginn seines Discours sur les sciences et les arts von 1750 eine der besten zeitgenössischen Definitionen der gesamteuropäischen Aufklärung und damit des programmatischen Selbstverständnisses einer Epoche, die sich schon seit der ersten Hälfte des 18. Jahrhunderts daran gewöhnt hat, sich stolz und selbstbewußt als das “siècle des lumières” und als “siècle éclairé” zu benennen. Bevor er die Preisfrage der Académie de Dijon (“Si le rétablissement des sciences et des arts a contribué à épurer les mœurs”) im Namen von Natürlichkeit, Tugend und Moral mit einer Kampfansage gegen den rationalistischen Optimismus und einer vielfach variierten Diatribe gegen Wissenschaftsgläubigkeit und gesellschaftliche Dekadenz und Entfremdung beantwortet, formuliert Rousseau eine Art Hymne an diese Entwicklung der abendländischen Gesellschaft"))
my_list = nlp("Niemand anderer als Jean-Jacques Rousseau - jener Aufklärer, der als einer der schärfsten Kritiker der “philosophes” à la Voltaire zu gelten hat und der früh die Widersprüche der bürgerlichen Aufklärung offenlegte - gibt zu Beginn seines Discours sur les sciences et les arts von 1750 eine der besten zeitgenössischen Definitionen der gesamteuropäischen Aufklärung und damit des programmatischen Selbstverständnisses einer Epoche, die sich schon seit der ersten Hälfte des 18. Jahrhunderts daran gewöhnt hat, sich stolz und selbstbewußt als das “siècle des lumières” und als “siècle éclairé” zu benennen. Bevor er die Preisfrage der Académie de Dijon (“Si le rétablissement des sciences et des arts a contribué à épurer les mœurs”) im Namen von Natürlichkeit, Tugend und Moral mit einer Kampfansage gegen den rationalistischen Optimismus und einer vielfach variierten Diatribe gegen Wissenschaftsgläubigkeit und gesellschaftliche Dekadenz und Entfremdung beantwortet, formuliert Rousseau eine Art Hymne an diese Entwicklung der abendländischen Gesellschaft")
my_list_2 = nlp(text)
print(my_list_2)

file = open("output.csv", "w", encoding="utf-8")
for i in range(len(my_list)):
    print(my_list[i])
    my_id = my_list[i]
    file.write((str(my_id)))

file2 = open("output2.csv", "w", encoding="utf-8")
for i in range(len(my_list_2)):
    print(my_list_2[i])
    my_id2 = my_list_2[i]
    file2.write((str(my_id2)))
