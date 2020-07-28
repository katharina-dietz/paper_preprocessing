import polyglot
import polyglot.downloader

# die Installation war hakelig, wg Decoding-Problemen in den readme-files *augenroll*
# der treebank und korpusdownload vom server funktioniert nicht *kotz*
# zeitverschwendung? nur rein in paper, wenn es sein muss

with open("../data_in/rieger.txt", encoding="utf-8") as file:
    text = file.read()