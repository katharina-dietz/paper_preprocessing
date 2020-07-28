from __future__ import division
import nltk
tc = nltk.classify.textcat.TextCat()

# Es soll segmentweise bestimmt werden, ob der Text gerade auf franzöisch oder auf deutsch geschrieben ist


langs = [
    "German-UTF8",
    "French-UTF8",
]


with open("../data_in/rieger.txt", encoding="utf-8") as file:
    data = file.read()
tokens = nltk.tokenize.word_tokenize(data)

print(tokens)

sentences = nltk.sent_tokenize(data)

guess = tc.guess_language("Dies ist ein Beispieltext auf Deutsch.")
print(guess)

for word in tokens:
    guess_all = tc.guess_language(word)
    print(guess_all)


"""
ne_tagged = nltk.ne_chunk(pos_tagged)
print(ne_tagged)
"""
"""
file = open("../data_out/paper_nltk.csv", "w", encoding="utf-8")
for word in ne_tagged:
    file.write(str(word) + "\n")
"""