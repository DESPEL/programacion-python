from random import shuffle
import random
import re


words = {}
with open("palabras.txt", "r", encoding="utf-8") as fp:
    for w in fp.readlines():
        w = w.strip().upper()
        if re.match(r"[^A-Za-z]+", w):
            continue

        if not len(w) in words.keys():
            words[len(w)] = [w, ]
        else:
            words[len(w)].append(w)


class Word:
    @staticmethod
    def get(length=10) -> str:
        words[length] = words[length][0:1000]
        shuffle(words[length])
        return random.choice(words[length])

    @staticmethod
    def get_special(expr, max_len):
        lengths = [x for x in range(4, max_len+1)]
        shuffle(lengths)
        for l in lengths:
            if l not in words.keys():
                continue
            elements = list(filter(expr, words[l]))
            if len(elements) > 0:
                w = random.choice(elements)
                words[l].remove(w)
                return w
        return None
