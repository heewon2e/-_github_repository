# -*- coding: utf-8 -*-
"""Untitled16.ipynb의 사본

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aNirVghUtiqOsEiZJNahnL4xEpA8pVEx
"""


def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(radius):
    area = 3.14 * radius ** 2
    return area

input_r = '넓이를 구하고자 하는 원의 반지름은? '
result = get_radius(input_r)


area_r = get_circle_area(result)
print("반지름이", result,"인 원의 넓이 = ","3.14*",result,"*",result,"=",area_r)
