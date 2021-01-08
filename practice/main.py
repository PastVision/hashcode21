#   Google Hashcode 2021
#   TeamKernelPanic!
#   Practice Problem
#
#   TODO : 

import sys

if __name__ == '__main__':
    if len(sys.argv)<2:
        print('Usage: main.py filename')
    else:
        pizzas = list()
        with open(sys.argv[1],'rt') as f:           #Set to Open a_example in launch.json
            m, t2, t3, t4 = map(int, f.readline().split())                      #m = no. of pizzas, tn = no. of teams of n people
            pizzas = [x.rstrip('\n').split() for x in f.readlines()]            #Will be optimized later
            pizzas = [{'ingQty':x[0], 'ing':x[1:]} for x in pizzas]             #ingQty = No. of ingredients, ing = ingredients
            print(pizzas)