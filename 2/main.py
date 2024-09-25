"""
6. Написать функцию, которая принимает список, состо-
ящий из n элементов, и возвращает количество целых чисел и
чисел с плавающей точкой.
"""

from generateNumbers import generateTenNumber

def foo(arr):
    int_arr = []
    float_arr = []
    
    for i in arr:
        if type(i).__name__ == "int":
            int_arr.append(i)
        elif type(i).__name__ == "float":
            float_arr.append(i)
            
    return f'Целый чисел - {len(int_arr)}\nЧисел с плавающей точкой {len(float_arr)}'


test_arr = generateTenNumber() # генерирую числа

print('исходный список чисел -', test_arr)

print('\nВывод функции - \n')
print(foo(test_arr))