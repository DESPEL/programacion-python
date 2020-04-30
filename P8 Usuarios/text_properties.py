from collections.abc import Mapping


class TextProperties(Mapping):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __getitem__(self, name):
        return self.kwargs[name]

    def __len__(self):
        return len(self.kwargs)

    def __iter__(self):
        return iter(self.kwargs)
