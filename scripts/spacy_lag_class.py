import spacy
from spacy_langdetect import LanguageDetector
import en_core_web_sm
import de_core_news_sm


nlp = en_core_web_sm.load()
nlp.add_pipe(LanguageDetector(), name="language_detector", last=True)
text = "This is an English text. Dies ist ein deutscher Text. C'est la texte francaise."
doc = nlp(text)
# document level language detetion. Think of it like average language of the document.
print(doc._.language)
# sentence level language detection
for sent in doc.sents:
    print(sent, sent._.language)

for token in doc:
    print(token, token._.language)

# Sprachauswahl für Sprachbestimmung auf Tokenebene, um Ergebnisse zu verbessern
# https://code.google.com/archive/p/language-detection/wikis/FrequentlyAskedQuestion.wiki
