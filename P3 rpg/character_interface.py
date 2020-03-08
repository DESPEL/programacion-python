import abc


class CharacterInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, 'attack')
            and callable(subclass.defend)
            and hasattr(subclass, 'defend')
            and callable(subclass.defend)
            and hasattr(subclass, 'is_alive')
            and callable(subclass.is_alive)
        )
