import csv

abreviaciones = {}

with open("claves_estados.csv", "r", encoding="utf-8") as f:
    for data in csv.reader(f, delimiter="\t"):
        todo = data
        abreviaciones[todo[0].upper()] = todo[-1]
