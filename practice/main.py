import sys

if __name__ == '__main__':
    if len(sys.argv)<2:
        print('Usage: main.py filename')
    else:
        pizzas = list()
        with open(sys.argv[1],'rt') as f:           #Set to Open a_example in launch.json
            m, t2, t3, t4 = map(int, f.readline().split())
            pizzas = [x.rstrip('\n') for x in f.readlines()]            #Will be optimized later
            print(pizzas)