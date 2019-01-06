class Animal():
    def walk(self):
        print("걷는다")

    def eat(self):
        print("먹는다")

    def greet(self):
        print("인사한다")


class Cow (Animal):


class Human(Animal):

    def wave(self):
        print("손을 흔든다")

    def greet(self):
        self.wave()


class Dog(Animal):

    def wag(self):
        print("꼬리를 흔든다")

    def greet(self):
        self.wag()


COW = Cow()
cow.greet()

# 실습


class Car():

    def run(self):
        print("차가 달립니다.")


class Truck(Car):

    def load(self):
        print("짐을 실었습니다.")
    # 이 아래에서 run 메소드를 오버라이드 하세요.

    def run(self):
        print("트럭이 달립니다.")


truck = Truck()
truck.run()
