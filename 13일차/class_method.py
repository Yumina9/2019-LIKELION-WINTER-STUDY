class Human():

    def __init__(self, name, weight):
        #초기화 함수
        print("__init__실행")
        self.name = name
        self.weight = weight


    def __str__(self):
        #문자열의 함수
        return "{} (몸무게 {}kg)".format(self.name, self.weight)
  
    def eat(self):
        self.weight += 0.1
        print("{}가 먹어서 {}kg이 되었습니다".format(self.name, self.weight))
    def walk(self):
        self.weight -= 0.1
        print("{}가 걸어서 {}kg이 되었습니다.".format(self.name, self.weight))

person = Human("사람", 60.5)
print(person)

#실습

class Human():
    
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def __str__(self):
        return "{} (몸무게 {}kg)".format(self.name, self.weight)
    
    def eat(self):
        self.weight += 0.1
        print("{}가 먹어서 {}kg이 되었습니다.".format(self.name, self.weight))
    
    def walk(self):
        self.weight -= 0.1
        print("{}가 걸어서 {}kg이 되었습니다.".format(self.name, self.weight))

# 아래에서 person을 이름과 몸무게를 가지는 Human클래스의 인스턴스로 만들어보세요.
person = Human("사람", 60.5)
person.walk()
person.walk()
person.eat()