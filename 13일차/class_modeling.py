class Human():


person = Human()
person.name = '철수'
person.weight = 60.5


def create_human(name, weight):
    person = Human()
    person.name = name
    person.weight = weight
    return person


Human.create = create_human
person = Human.create("철수", 60.5)


def eat(person):
    person.weight += 0.1
    print("{}가 먹어서 {}kg이 되었습니다".format(person.name, person.weight))


def walk(person):
    person.weight -= 0.1
    print("{}가 걸어서 {}kg이 되었습니다.".format(person.name, person.weight))


Human.eat = eat
Human.walk = walk
person.walk()  # 철수가 걸어서 60.4kg이 되었습니다.
person.eat()  # 철수가 걸어서 60.5kg이 되었습니다.
person.walk()  # 철수가 걸어서 60.4kg이 되었습니다.
