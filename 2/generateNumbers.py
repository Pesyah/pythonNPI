import random

def generateTenNumber():
    int_numbers = random.randrange(0, 11)
    float_numbers = 10 - int_numbers

    int_numbers_array = []

    float_numbers_array = []

    for _ in range(int_numbers):
        int_numbers_array.append(random.randrange(0, 11))
        
    for _ in range(float_numbers):
        float_numbers_array.append(round(random.random() * 10, 3))
        
    return int_numbers_array + float_numbers_array