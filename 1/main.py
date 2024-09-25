"""
6. Написать функцию, которая принимает целочисленный
список, содержащий три элемента, и возвращает сумму этих
элементов.
"""

def foo(arr: list):
    # return sum(arr) # простое решение
    arr_sum = 0
    for i in arr:
        arr_sum += i
    return arr_sum # чуть более сложное


print(foo([1, 2, 3])) # 6
print(foo([100, 200, 300])) # 600
print(foo([33, 22, 11])) # 66