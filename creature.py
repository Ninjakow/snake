import random


class Creature:

    def __init__(self, traits=None):
        if traits == None:
            self.traits = [random.random() for i in range(10)]
        else:
            self.traits = traits


if __name__ == "__main__":
    a = Creature(1)
