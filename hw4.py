# -*- coding: utf-8 -*-
"""hw4

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1o0wPwwtGvPK8S1H5JFMqYFa-O6ywI4VK
"""



def draw_line_string(msg1, msg2, nstr):
  line = rep_char('-', nstr*2)
  print(line)
  print('',msg1)
  print('',msg2)
  print(line)


hello_gyopo = input("input his/her name :")
msg1 = 'Hello ' + hello_gyopo+','
msg2 = "welcome to Seoul"
nstr = len(msg1) if (len(msg1)>len(msg2)) else len(msg2)
draw_line_string(msg1, msg2, nstr)


# Max 사용

def draw_line_string(msg1, msg2, nstr):
  line = rep_char('-', nstr*2)
  print(line)
  print('',msg1)
  print('',msg2)
  print(line)


hello_gyopo = input("input his/her name :")
msg1 = 'Hello ' + hello_gyopo+','
msg2 = "welcome to Seoul"
nstr = max(len(msg1),len(msg2))
draw_line_string(msg1, msg2, nstr)

