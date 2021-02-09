import operator
from sys import argv
from os import listdir
from time import time
def countsameings(p1, p2): return len(p1+p2)-len(set(p1+p2))


class EvenMorePizza:

    class Pizza:
        def __init__(self, pizza, index):
            self.index = index
            self.ingredients = pizza
            self.count = len(pizza)

    class Delivery:
        def __init__(self):
            self.pizzas = list()

        def __len__(self):
            return len(self.pizzas)

        def calculate_score(self):
            uniq = set()
            for pizza in self.pizzas:
                uniq = uniq.union(set(pizza.ingredients))
            self.score = len(uniq)**2

    class Solution:
        def __init__(self):
            self.delivery_count = 0
            self.team2 = list()
            self.team3 = list()
            self.team4 = list()

        def addsoln(self, delivery):
            size = len(delivery)
            if size == 4:
                self.team4.append(delivery)
            elif size == 3:
                self.team3.append(delivery)
            elif size == 2:
                self.team2.append(delivery)
            self.delivery_count += 1

        def calculate_score(self):
            score = 0
            teams = [self.team2, self.team3, self.team4]
            for team in teams:
                for delivery in team:
                    score+=delivery.score
            self.score = score

        def __repr__(self):
            out = f'{self.delivery_count}\n'
            teams = [self.team2, self.team3, self.team4]
            for i,team in enumerate(teams):
                if len(team)>0:
                    for delivery in team:
                        out+=str(i+2)
                        for pizza in delivery.pizzas:
                            out+=' '+str(pizza.index)
                        out+='\n'
            return out


    def __init__(self, inputfile):
        self.teamlist = [0, 0]
        self.pizzas = list()
        self.filename = inputfile
        self.soln = self.Solution()
        with open(inputfile, 'rt') as f:
            self.PizzaCount, *temp = map(int, f.readline().split())
            self.teamlist += temp
            for idx, line in enumerate([x.rstrip('\n').split() for x in f.readlines()]):
                self.pizzas.append(self.Pizza(line[1:], idx))
            self.pizzas.sort(key=operator.attrgetter('count'), reverse=True)

    def solve(self):
        while len(self.pizzas) >= 2:
            possibledelSize = 0
            for teamsize in range(4,1,-1):
                if self.teamlist[teamsize] > 0:
                    possibledelSize = teamsize
                    break
            if possibledelSize == 0: break

            delivery = self.Delivery()
            delivery.pizzas.append(self.pizzas[0])
            self.pizzas.pop(0)
            deliveryUniqIngs = set(delivery.pizzas[0].ingredients)
            while len(delivery) < possibledelSize:
                nextidx = -1
                nextconflict = 0
                nextings = 0
                for i in range(len(self.pizzas)):
                    if self.pizzas[i].count < nextings: break
                    conflict = countsameings(list(deliveryUniqIngs),self.pizzas[i].ingredients)
                    newings = self.pizzas[i].count - conflict
                    if newings > nextings or (newings == nextings and conflict < nextconflict):
                        nextidx = i
                        nextconflict = conflict
                        nextings = newings
                        if nextconflict == 0: break
                if nextings == 0: break
                delivery.pizzas.append(self.pizzas[nextidx])
                deliveryUniqIngs = deliveryUniqIngs.union(self.pizzas[nextidx].ingredients)
                self.pizzas.pop(nextidx)
            if self.teamlist[len(delivery)] == 0:
                while len(self.pizzas) > 0:
                    delivery.pizzas.append(self.pizzas[-1])
                    self.pizzas.pop(-1)
                    if self.teamlist[len(delivery)] > 0: break
            self.teamlist[len(delivery)]-=1
            delivery.calculate_score()
            self.soln.addsoln(delivery)
            del delivery
        self.soln.calculate_score()

def saveoutput(f, data):
    with open(argv[2]+'/'+f+'.out','wt') as out:
        out.write(data)

if __name__ == '__main__':
    if len(argv) < 2:
        print('Invalid Input!\nUsage: python main.py <directory_containing_input_files> <output_directory>')
    else:
        files = listdir(argv[1])
        score = 0
        start = time()
        for f in files:
            solver = EvenMorePizza(argv[1]+'/'+f)
            solver.solve()
            temp = solver.soln.score
            print('Score for {} is {}'.format(f, temp))
            score += temp
            saveoutput(f,solver.soln.__repr__())
        total = time() - start
        print('Total {}, Time Taken: {}'.format(score, total))
