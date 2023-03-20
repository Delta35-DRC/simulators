class Constructor:
    num = 0

    def __init__(self, entity, age):
        Constructor.num += 1
        self.entity = entity
        self.age = age
        print(f"Constructed entity {self.entity}, age {self.age}")


class Human(Constructor):
    num = 0

    def __init__(self, entity, age, mood, cur, work):
        Human.num += 1
        self.cur = cur
        self.work = work
        print(f"Augmented {self.entity} with {self.cur} currency, work - {self.work}")


class Animal(Constructor):
    num = 0

    def __init__(self, entity, age, race):
        Animal.num += 1
        self.race = race


s1 = Human('01', 30, 50, 500, 'cleaner')
s2 = Human('02', 25, 75, 250, 'engineer')
s3 = Human('03', 21, 75, 500, 'driver')
s4 = Animal('04', 6, 'cat')
s5 = Animal('05', 4, 'turtle')
print(f'Constructor.num = {Constructor.num}')


def processor_1h(self, entity, age, mood, currency, work):
    pass


def processor_2a(self, entity, age, race):
    pass
