abreviaciones = {}

with open("claves_estados.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        todo = line.strip().split("\t")
        abreviaciones[todo[0].upper()] = todo[-1]
