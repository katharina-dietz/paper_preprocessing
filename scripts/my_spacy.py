import spacy
from spacy_langdetect import LanguageDetector
# Skript zur Tokenisierung, Sprachbestimmung, POS-Tagging, NER
# Ergebnisse: ziemlich gut. Erkennt auch ohne weiters Zutun mehrteilige Namen als Einheit
# Noch keine Unterscheidung in deutsche und französische Textteile, bis jetzt rein deutsch
# Info Spracherkennung: https://spacy.io/universe/project/spacy-langdetect


def preprocessing():

    # Deutsches und Französisches Sprachmodell laden
    nlp_de = spacy.load("de_core_news_md")
    nlp_fr = spacy.load("fr_core_news_sm")

    # Language Detector laden
    nlp_de.add_pipe(LanguageDetector(), name="language_detector", last=True)

    # Den zu untersuchenden Text öffen
    with open("../data_in/rieger.txt", encoding="utf-8") as file:
        text = file.read()
    # dem Text wird ein deutsches Sprachmodell zugewiesen
    # --> wird gleich geändert, erst Spracherkennung, dann Sprachmodell de oder fr

    doc = nlp_de(text)

    # Bestimmung der Sprache auf Dokumentebene
    print(doc._.language)

    dict_fr = {}
    dict_de = {}
    dict_all = {}
    dict_sonstiges = {}

    for sent in doc.sents:
        dict_all[sent] = sent._.language

    print(type(doc.sents))

    print(dict_all)

    for i in dict_all:
        if "fr" in dict_all[i]['language']:
            dict_fr[i] = dict_all[i]
        if "de" in dict_all[i]['language']:
            dict_de[i] = dict_all[i]
        else: dict_sonstiges = dict_all[i]
    # print(dict_fr)
    # print(dict_de)
    # print(dict_sonstiges)


    ##############################
    text_fr = []
    file = open("../data_out/spacy_lfr.txt", "w", encoding="utf-8")

    for j, k in dict_fr.items():
        print("Text:", j)
        file.write(str(j))
        for m in k:
            print(m + ":", k[m])

    file2 = open("../data_out/spacy_lde.txt", "w", encoding="utf-8")

    for n, o in dict_de.items():
        print("Text:", n)
        file2.write(str(n))


# preprocessing()

nlp_de = spacy.load("de_core_news_md")
with open("../data_out/spacy_lde.txt", encoding="utf-8") as file:
    text = file.read()

doc = nlp_de(text)

# Analyse syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)

# next to do: syntaxinformationen für  ner utilitarisieren
# Was mache ich mit französischen Häppchen?


file = open("../data_out/paper_spacy.csv", "w", encoding="utf-8")
for entity in doc.ents:
    file.write(str(entity.text) + ",")
    file.write(str(entity.label_) + "\n")

