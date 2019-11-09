# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
s_input = """
3

4 5 x | x x x | x 3 x 
7 x x | x x 3 | x 9 1 
3 x 6 | x 1 x | 4 5 x 
---------------------
9 x x | 7 x 5 | x x 6 
6 x x | 1 x 9 | x x 5 
8 x x | 6 x 4 | x x 9 
---------------------
x 6 4 | x 7 x | 5 x 3 
2 7 x | 3 x x | x x 4 
x 3 x | x x x | x 7 8 
"""

print (s_input)

print ("*****************************")
i = 0
first_number = False

for line in s_input.splitlines():
    print (str(i) + " " + line + " " + str(len(line)))
    i = i + 1

    if ((first_number == False) and len(line) == 1):
        size = int(line) * int(line)
        break

        arr = [s_input]
    print(arr[0][0])

print (size)

# for line in s_input.splitlines():
