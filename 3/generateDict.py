import random

def generateDict():
    numbers = random.randrange(0, 11)
    new_dict = dict()
    
    for i in range(numbers):
        new_dict[i] = "foo"
    return new_dict