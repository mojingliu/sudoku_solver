# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
s_input = """
3

x x x | x x x | x x x
x 1 x | 6 2 x | x 9 x
x x 2 | x x 9 | 3 1 x
---------------------
x x 4 | x x 6 | x 8 x
x x 8 | 7 x 2 | 1 x x
x 3 x | 8 x x | 5 x x
---------------------
x 6 9 | 1 x x | 4 x x
x 8 x | x 7 3 | x 5 x
x x x | x x x | x x x
"""

size = 0

def main():
    print (s_input)
    global size
    print ("*****************************\n")
    i = 0
    first_number = False

    for line in s_input.splitlines():
        if len(line) == 1:
            size = int(line)
            break

    rows, cols = (size*size, size*size)
    arr = [[0 for i in range(cols)] for j in range(rows)]
    i=0
    j=0
    increment = False
    for line in s_input.splitlines():
        line = line.strip('-|')
        if len(line) > size*size:
            for char in line.split(' '):
                increment = False
                if char.isdigit():
                    arr[j][i] = int(char)
                    i = i + 1
                elif char == 'x' :
                    arr[j][i] = 0
                    i = i + 1
            i = 0
            j = j + 1

    for row in arr:
        print row

    arr  = _solver_(arr)
    print ("*****************************\n")

    for row in arr:
        print row


def _solver_(sudoku):

    for j in range(0,len(sudoku[0])):
        for i in range(0, len(sudoku[0])):
            #solves for only 1 number
            if sudoku[j][i] == 0:
                #print j,i
                for n in range(1,size*size): # try different number
                    if try_number(i,j,sudoku,n): # good number
                        #print "recursion"
                        sudoku = _solver_(sudoku)  # try to solve it with this good number
                        if sudoku[j][i] == 0: # if the spot we tried came back negative
                            continue   # we need to try next number
                        else:
                            solved = True
                            for l in range(0, len(sudoku[0])):
                                if not solved :
                                    break
                                for m in range(0, len(sudoku[0])):
                                    if sudoku[l][m] == 0:
                                        solved = False
                                        break
                            if solved:
                                return sudoku


                    else:
                        #print "reset"        # if there is no possible good number, reset the current number and go back
                        sudoku[j][i] = 0
                        return sudoku

    #print "here"
    return sudoku


def _check_correct_(i,j,sudoku):
    return check_ver(i,j,sudoku) and check_hor(i,j,sudoku) and check_box(i,j,sudoku)

def check_ver(i,j,sudoku):
    for k in range(0,size*size):
        if sudoku[k][i] == sudoku[j][i] and k != j:
            return False
    return True

def check_hor(i,j,sudoku):
    for k in range(0,size*size):
        if sudoku[j][k] == sudoku[j][i] and k != i:
            return False
    return True

def check_box(i,j,sudoku):
    for k in range(j-j%size,j-j%size+size):
        for m in range(i-i%size,i-i%size+size):
            if sudoku[k][m] == sudoku[j][i] and k != j and m != i:
                return False
    return True

def try_number(i,j,sudoku,tries):
    attempt = 1
    for num in range(1,size*size+1):
        #print "Trying for " +str(j) + " " + str(i) + " " + str(num)
        sudoku[j][i] = num
        if _check_correct_(i,j,sudoku):
            #print "found a good number " + str(num) + " " + str(attempt) + "/" + str(tries)
            if attempt == tries :
                return True
            else:
                attempt = attempt + 1
    #print "didnt find anything"
    return False


if __name__ == "__main__":
    main()