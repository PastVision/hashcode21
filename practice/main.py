import sys

if __name__ == '__main__':
    if len(sys.argv)<2:
        print('Usage: main.py filename')
    else:
        with open(sys.argv[1],'rt') as f:
            pass