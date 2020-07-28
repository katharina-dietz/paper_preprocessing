import nltk
nltk.download("punkt")
with open("../data_in/rieger.txt", encoding="utf-8") as file:
    data = file.read()

tokens = nltk.tokenize.word_tokenize(data)

file = open("../data_out/trainingsgrundlage.csv", "w", encoding="utf-8")

for word in tokens:
    file.write(str(word) + "\n")