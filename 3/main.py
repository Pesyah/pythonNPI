"""
6. Написать функцию, которая принимает словарь и с по-
мощью генераторного выражения создает и возвращает новый
список, содержащий значения ключей входящего словаря.
"""


from generateDict import generateDict

def foo(test_dict: dict):
    keys_array = []
    
    for i in test_dict:
        keys_array.append(i)
        yield keys_array
    
new_dict = generateDict()

print('Исходный словарь -', new_dict)

new_generator = foo(new_dict)

for i in range(len(new_dict)):
    print(next(new_generator))