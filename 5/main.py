"""
6. Написать функцию, которая принимает путь к HTML
файлу и html тег («p», «h1», «article» и др.) и возвращает коли-
чество повторений полученного тега в файле с учетом того, что
требуется вернуть только количество тегов, который имеет от-
крывающую и закрывающую часть.
"""
import os


def foo(fileName, tag):
    with open(fileName, 'r') as f:
        file = f.read()
        tags = min([file.count(f'<{tag}'), file.count(f'</{tag}>')])
        return f'количество ВЕРНЫХ тегов <{tag}> - {tags}'

print(foo(os.getcwd() + '\\5\\main.html', 'p'))
print(foo(os.getcwd() + '\\5\\main.html', 'h2'))
print(foo(os.getcwd() + '\\5\\main.html', 'article'))

"""
Для теста можно зайти в файлик и добавить рандомно местами
<p> или </p>,
"""