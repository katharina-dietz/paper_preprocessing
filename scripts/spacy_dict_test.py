from spacy_langdetect import LanguageDetector
import de_core_news_sm
import nltk


text_gesamt = "Dies ist ein deutscher Text. C'est la texte francaise. J'aime des pommes. Und jetzt wieder auf Deutsch. C'est la vie. Alle zusammen tanzt das Brot."
nlp = de_core_news_sm.load()
nlp.add_pipe(LanguageDetector(), name="language_detector", last=True)
doc = nlp(text_gesamt)

text_gesamt = nltk.sent_tokenize(text_gesamt)
print(text_gesamt)

dict_fr = {}
dict_de = {}
dict_all = {}
dict_en = {}
dict_sonstiges = {}
for sent in doc.sents:
    dict_all[sent] = sent._.language

print(type(doc.sents))

print(dict_all)

for i in dict_all:
    if "fr" in dict_all[i]['language']:
        print("na endlich")
    else: print("nope")

for i in dict_all:
    if "fr" in dict_all[i]['language']:
        dict_fr[i] = dict_all[i]
    if "de" in dict_all[i]['language']:
        dict_de[i] = dict_all[i]
    if "en" in dict_all[i]['language']:
        dict_en = dict_all[i]
    else: dict_sonstiges = dict_all[i]
print(dict_fr)
print(dict_de)
print(dict_en)
print(dict_sonstiges)
einfaches_dict = {"erster key value": "dies ist ein Test", 2: "C'est la une test."}
print(einfaches_dict["erster key value"])
for i in einfaches_dict:
    print(einfaches_dict[i])

verschachteltes_dict = {1: {"bla": "string", "blub": "noch ein String"}, 2: {"bla": "string", "blub": "noch ein String"}}

print(verschachteltes_dict[1]["blub"])

"""
#Erstelle (aus der Liste[diese Info kann dabei stehen, muss aber nicht]) ein Dictionary und zähle für jedes Wort, wie oft es vorkommt. 
#Lösung
Dict={}
for i in tokens:
  if i in Dict:
    Dict[i] += 1
  else:
    Dict[i] = 1
print(Dict)

"""