def func():
    return {"a": {}}


def c(d):
    d["a"] = "b"
    return d


a = func()
b = c(a["a"])

print(a)
print(b)
