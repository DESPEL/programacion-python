class hola:
    def __enter__(self):
        print("asdasd")

    def __exit__(self, *args):
        print(args)


with hola() as h:
    print(h)