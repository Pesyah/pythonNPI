"""
6. Написать функцию, которая принимает путь к изобра-
жению и поворачивает его на 90 градусов, сохраняя его по тому
же пути.
"""
from PIL import Image

def foo(imagePath):
    img = Image.open(imagePath).rotate(90)
    img.save(imagePath)
    
foo('8/img.jpg')