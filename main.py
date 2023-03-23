from random import randint
import time
dvd = 0


class Constructor:

    def __init__(self, entity, age):
        self.entity = entity
        self.age = age
        print(f"Constructed entity {self.entity}, age{self.age}")


class Human(Constructor):
    alive = True
    money = randint(100, 750)
    job = None
    home = None
    eat = 70
    sleep = 70
    mood = 70

    def work(self):
        if self.job:
            if self.job == 'IT':
                self.money += 200
            elif self.job == 'Engineer':
                self.money += 175
            elif self.job == 'Office':
                self.money += 100
            elif self.job == 'Cleaner':
                self.money += 80
            self.mood -= 10
            self.sleep -= 25
            self.eat -= 20
            print(f"{self.entity} worked, money {self.money}, mood {self.mood}, sleep {self.sleep}, eat {self.eat}")

    def sleepact(self):
        self.mood += 5
        self.sleep += 80
        self.eat -= 30
        print(f"{self.entity} slept, mood {self.mood}, sleep {self.sleep}, eat {self.eat}")

    def rest(self):
        self.mood += 25
        self.money -= 25
        self.sleep -= 20
        self.eat -= 20
        print(f"{self.entity} rested, money {self.money}, mood {self.mood}, sleep {self.sleep}, eat {self.eat}")

    def eatact(self):
        self.eat += 80
        self.money -= 25
        self.mood += 5
        print(f"{self.entity} ate, money {self.money}, mood {self.mood}, eat {self.eat}")

    def nothing(self):
        if self.entity != 'Mr. Jules Archibald':
            print(f"{self.entity} does nothing")
        else:
            global dvd
            print("Mr. Jules Archibald is making his jump-scare DVDs again!")
            dvd += 1

    def selector(self):
        if (randint(0, 50) == 0 and self.alive) or (self.age > 80):
            self.alive = False
            if self.entity != 'Mr. Jules Archibald':
                print(f"{self.entity} is dead")
            else:
                print("Mr. Jules Archibald is no more making jump-scare DVDs now")
        if self.alive:
            if not self.job:
                jobpick = randint(0, 3)
                if jobpick == 0:
                    self.job = 'IT'
                elif jobpick == 1:
                    self.job = 'Engineer'
                elif jobpick == 2:
                    self.job = 'Office'
                elif jobpick == 3:
                    self.job = 'Cleaner'
            if not self.home:
                homepick = randint(0, 1)
                if homepick == 0:
                    self.home = 'Private house'
                elif homepick == 1:
                    self.home = 'Flat'
            self.age += 0.5
            print(f"{self.entity} is {self.age}")
            self.money -= 20
            print(f"Tax payment 20 {self.entity}, money {self.money}")
            if self.eat <= 30:
                self.eatact()
            elif self.sleep <= 20:
                self.sleepact()
            elif self.money <= 250:
                self.work()
            elif self.mood <= 25:
                self.rest()
            else:
                self.nothing()
            print(f"{self.entity}, age {self.age}, alive {self.alive}, money {self.money}, job {self.job}, "
                  f"home {self.home}, eat {self.eat}, sleep {self.sleep}, mood {self.mood}")


class Animal(Constructor):
    alive = True
    ownerpick = randint(0, 2)
    if ownerpick == 0:
        owner = 'Andreyka'
    elif ownerpick == 1:
        owner = 'Ivan'
    elif ownerpick == 2:
        owner = 'Mr. Jules Archibald'
    homepick = randint(0, 1)
    if homepick == 0:
        home = 'FB4-5'
    elif homepick == 1:
        home = 'FB7-2'

    def selector(self):
        if (randint(0, 50) == 0 and self.alive) or (self.age > 20):
            self.alive = False
            print(f"{self.entity} is dead")
        else:
            self.age += 0.5
            print(f"{self.entity} is {self.age}")


# class House:
    # def __init__(self, entity, cap, rsd):
        # self.entity = entity
        # self.cap = cap
        # self.rsd = rsd
        # print(f"Constructed house {self.entity}, cap{self.cap}, rsd{self.rsd}")

    # def explode(self):
        # print(f"{self.entity} boom")
        # del self.entity
        # del self.rsd


e1 = Human('Andreyka', 20)
e2 = Human('Ivan', 25)
e3 = Human('Mr. Jules Archibald', 40)
e4 = Animal('Sonya', 5)
# e5 = House('FB4-5', 20, [e1, e2, e4])
# e6 = House('FB7-2', 20, [e3])

print("Default tick speed is 5 seconds")
print("With default, 10 cycles will be 50 seconds long")
for i in range(10):
    time.sleep(5)
    e1.selector()
    e2.selector()
    e3.selector()
    e4.selector()

print("----------STATISTICS----------")
print("-----|Alive:")
print(f"{e1.entity}:{e1.alive}")
print(f"{e2.entity}:{e2.alive}")
print(f"{e3.entity}:{e3.alive}")
print(f"{e4.entity}:{e4.alive}")
print("-----|Mood:")
print(f"{e1.entity}:{e1.mood}")
print(f"{e2.entity}:{e2.mood}")
print(f"{e3.entity}:{e3.mood}")
print("-----|Age:")
print(f"{e1.entity}:{e1.age}")
print(f"{e2.entity}:{e2.age}")
print(f"{e3.entity}:{e3.age}")
print(f"{e4.entity}:{e4.age}")
print("-----|Money:")
print(f"{e1.entity}:{e1.money}")
print(f"{e2.entity}:{e2.money}")
print(f"{e3.entity}:{e3.money}")
print("------------------------------")
print(f"Total jump-scare DVDs made by Mr. Jules Archibald: {dvd}")
