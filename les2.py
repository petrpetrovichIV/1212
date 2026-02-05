import random
from random import choice


class Student:

    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.skills = skills = 5

    def hello(self):
        print(f'hi. i am {self.name}! iam {self.year}')
        print(f'my skilass is {self.skills:.2f} brain point')


    def grow_up(self):
        self.year += 1

    def study(self):
        self.skills += 0.5

    def chiil(self):
        self.skills -= 0.4

mark = Student("mark", 13)

for day in range(1,366):
    print(f'------- day {day} -------')

    choice = random.randint(0,1)

    if choice == 0:
        mark.study()
        print('stuffing...')
    else:
        mark.chiil()
        print('chilling.....')

mark.grow_up()
mark.hello()