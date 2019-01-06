class Animal():
    def walk(self):
        print("걷는다")

    def eat(self):
        print("먹는다")


class Human(Animal):

    def wave(self):
        print("손을 흔든다")


class Dog(Animal):

    def wave(self):
        print("꼬리를 흔든다")


person = Human()
person.walk()
person.eat()
person.wave()

dog = Dog()
dog.walk()
dog.eat()
dog.wave()

# 실습


class Car():

    def run(self):
        print("차가 달립니다.")

# 아래에서 Car를 상속받는 Truck이라는 클래스를 만들고, load라는 메소드를 만들어 보세요.


class Truck(Car):
    def load(self):
        print("짐을 실었습니다.")
# load메소드에서는 "짐을 실었습니다."라고 출력하면 됩니다.
