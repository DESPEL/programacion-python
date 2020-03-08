#import re;print([lambda words:[words, [words[len(word)].append(word) if len(word) in words.keys() else words.update({len(word):[word]}) for word in [x.strip().upper() for x in open("palabras.txt", "r", encoding="utf-8").readlines() if not re.match(r"[^A-Za-z]+", x.strip().upper())]]][0]][0]({}))


import re;[
    lambda var, funcs:
        [
            var.update({"palabras": [funcs["load_words"](),]}),
            funcs["add_word"](var["palabras"][0]),
            print(var["palabras"][0])
        ],
][0](
    {

    },
    {
        "load_words" : lambda: [lambda words: 
            [words, [words[len(word)].append(word) 
                if len(word) in words.keys() else 
                    words.update({len(word):[word]}) 
                    for word in [x.strip().upper() 
                        for x in open(
                                "palabras.txt", 
                                "r", 
                                encoding="utf-8"
                            ).readlines() 
                            if not re.match(
                                r"[^A-Za-z]+", 
                                x.strip().upper()
                            )
                ]
            ]][0]
        ][0]({}),
        "add_word" : lambda palabras: palabras[1].append("roiegjasoidjs")
    }
)

"""
import re;print([lambda words:
    [words, [words[len(word)].append(word) 
        if len(word) in words.keys() else 
            words.update({len(word):[word]}) 
            for word in [x.strip().upper() 
                for x in open(
                        "palabras.txt", 
                        "r", 
                        encoding="utf-8"
                    ).readlines() 
                    if not re.match(
                        r"[^A-Za-z]+", 
                        x.strip().upper()
                    )
        ]
    ]][0]
][0]({}))

"""
#a = type("Prueba", (), {
#    "print": lambda x: print('abcdefg' + str(x))
#})
#print(type(a))