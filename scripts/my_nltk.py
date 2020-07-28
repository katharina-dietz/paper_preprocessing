from __future__ import division
import nltk
nltk.download("punkt")

# funktioniert schlecht, weil man das NER-Tool selbst vortrainieren muss, wir aber bis jetzt wenig Text haben
# Außerdem wäre es schön, wenn man auf was vortrainiertes zurückgreifen könnte

with open("../data_in/rieger.txt", encoding="utf-8") as file:
    data = file.read()
tokens = nltk.tokenize.word_tokenize(data)

print(tokens)

sentences = nltk.sent_tokenize(data)

pos_tagged = nltk.pos_tag(tokens)

ne_tagged = nltk.ne_chunk(pos_tagged)
print(ne_tagged)

file = open("../data_out/paper_nltk.csv", "w", encoding="utf-8")

for word in ne_tagged:
    file.write(str(word) + "\n")


### man braucht ein selbstrainiertes 