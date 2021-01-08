#   Google Hashcode 2021
#   TeamKernelPanic!
#   Even More Pizza
#   Practice Problem
#
#   TODO : 

import sys

class EvenMorePizza:

    best_soln = {
        'D':0
    }
    best_score = 0

    def __init__(self, inputFile):
        with open(inputFile, 'rt') as f:
            self.M, self.T2, self.T3, self.T4 = map(int, f.readline().split())
            temp = [x.rstrip('\n').split() for x in f.readlines()]
            self.PIZZAS = [{'I':int(x[0]), 'ING':x[1:]} for x in temp]

    def solve(self):
        pass

    def best(self, solution):
        #INPUT
        # 5 1 2 1
        # 3 onion pepper olive              0
        # 3 mushroom tomato basil           1
        # 3 chicken mushroom pepper         2
        # 3 tomato mushroom basil           3
        # 2 chicken basil                   4

        #CALCULATE SCORE
        #EXAMPLE OUTPUT, SCORE = 65 = 49+16
        #2                  D (deliveries) = 2 Teams got pizza
        #2 1 4              T2 team I=5, 4(omitting repeated basil) SCORE = 4^2 = 16
        #3 0 2 3            T3 team I=9, 7(omitting repeated pepper mushroom) = 7^2 = 49
        score = 0
        for D in range(solution['D']):
            ings = list()
            for i in range(1, solution[str(D)][0]+1):
                pizza_idx = solution[str(D)][i]
                ings+=self.PIZZAS[pizza_idx]['ING']
            score += len(set(ings))**2

        #Compare
        if score > self.best_score:
            self.best_soln, self.best_score = solution, score
        elif score == self.best_score and solution['D'] > self.best_soln['D']:
            self.best_soln = solution

testSol = {
    'D':2,
    '0':[2, 1, 4],
    '1':[3, 0, 2, 3]
}

if __name__ == '__main__':
    if len(sys.argv)<2:
        print('Usage: main.py filename')
    else:
        Result = EvenMorePizza(sys.argv[1])
        #Result.solve()
        Result.best(testSol)
        print(Result.best_score,Result.best_soln)
