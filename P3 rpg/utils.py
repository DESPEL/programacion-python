import random


def random_event(probability) -> bool:
    val = random.randint(0, 99)
    return val < probability * 100
