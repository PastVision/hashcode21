# Google Hashcode 2021
# Qualifier Problem Solution
# Team Kernel-Panic

import sys
from os import listdir

class Street:
    def __init__(self,data) -> None:
        self.start = int(data[0])
        self.end = int(data[1])
        self.name = data[2]
        self.time = int(data[3])
        self.carcount = 0
        self.score = 0

class Car:
    def __init__(self, count) -> None:
        self.pathlen = count
        self.path = list()
        self.timeneeded = 0

    def makepath(self,simtime):
        time = 0
        for street in self.path:
            time += street.time
        time = (simtime-time)/simtime
        self.timeneeded = time if time>0 else 0

class Intersection:
    def __init__(self, id) -> None:
        self.id = id
        self.incomingStreets = dict()
        self.outgoingStreets = dict()
        self.incomingIntersections = dict()
        self.outgoingIntersections = dict()
        self.signalConfig = list()
def _LCM(a, b):
    if a > b:
        num1 = a
        num2 = b
    else:
        num1 = b
        num2 = a
    for i in range(1,num2+1):
        if (num1 * i) % num2 == 0:
            return i * num1
    return num2
def LCM(nums):
    if len(nums) < 2: return len(nums)
    if len(nums) == 2: return _LCM(nums[0], nums[1])
    return _LCM(nums[0],LCM(nums[1:]))

class SignalControl:
    def __init__(self, street, time) -> None:
        self.street = street
        self.time = time

class Solution:
    def __init__(self, intersections, time, bonus, cars) -> None:
        self.intersections = intersections
        self.time = time
        self.bonus = bonus
        self.cars = cars

    def writetofile(self, filename):
        with open(filename, 'wt') as f:
            signalscontrolled = [intersection for intersection in self.intersections if len(intersection.signalConfig)>0]
            f.write(f'{len(signalscontrolled)}\n')
            for intersection in signalscontrolled:
                f.write(f'{intersection.id}\n{len(intersection.signalConfig)}\n')
                for signal in intersection.signalConfig:
                    f.write(f'{signal.street.name} {signal.time}\n')



class Qualifier:

    def __init__(self, filename) -> None:
        self.streets = dict()
        self.intersections = dict()
        self.cars = list()
        with open(filename, 'rt') as f:
            self.TIME, I, S, V, self.BONUS = map(int, f.readline().split())
            for _ in range(S):
                streetdata = f.readline().split()
                street = Street(streetdata)
                self.streets[street.name] = street
                if street.start not in self.intersections:
                    self.intersections[street.start] = Intersection(street.start)
                if street.end not in self.intersections:
                    self.intersections[street.end] = Intersection(street.end)
                self.intersections[street.end].incomingIntersections[street.start]=self.intersections[street.start]
                self.intersections[street.end].incomingStreets[street.name]=street
                self.intersections[street.start].outgoingIntersections[street.end]=self.intersections[street.end]
                self.intersections[street.start].outgoingStreets[street.name]=street

            for _ in range(V):
                cardata = f.readline().split()
                car = Car(int(cardata[0]))
                car.path = [self.streets[street] for street in cardata[1:]]
                car.makepath(self.TIME)
                self.cars.append(car)

    def solve(self):
        startinggrid = set()
        for car in self.cars:
            startinggrid.add(car.path[0].name)
            for street in car.path:
                street.carcount += car.timeneeded
                street.score += car.timeneeded

        for intersection in self.intersections:
            intersection = self.intersections[intersection]
            streets = intersection.incomingStreets
            carstopass = 0
            times = list()
            for street in streets:
                street = streets[street]
                carstopass += street.score
            if carstopass == 0 : continue
            lcm = LCM([int(streets[street].score/carstopass*10) for street in streets])
            for street in streets:
                street = streets[street]
                if street.score != 0:
                    time = int(street.score/carstopass*10)
                    if time != 10:
                        if lcm == time: time = 10
                        else:
                            time = round(time*0.1)
                            if time<1: time = 1
                    else: time = 1
                    intersection.signalConfig.append(SignalControl(street,time))
            intersection.signalConfig.sort(key=lambda x: 1 if x.street.name in startinggrid else 0,reverse=True)
        self.solution = Solution(
            [self.intersections[intersection] for intersection in self.intersections],
            self.TIME,
            self.BONUS,
            self.cars
        )






if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Invalid Input!\nUsage: python main.py <directory_containing_input_files> <output_directory>')
    else:
        files = listdir(sys.argv[1])
        for f in files:
            solver = Qualifier(f'{sys.argv[1]}/{f}')
            solver.solve()
            solver.solution.writetofile(f"{sys.argv[2]}/{f.replace('.txt','.out')}")


