class Human():
person1 = Human()
person2 = Human()

a = list()
a   #[]
isinstance(a,list)  #True
list1 = [1, 2, 3]
list1  #[1, 2, 3]
list1.append(4)
list1  #[1, 2, 3, 4]

person1.language = '한국어'
preson2.language = 'English'
print(person1.language)  #한국어
print(person2.language)  #English
person1.name = '서울시민'
person2.name = '인도인'
def speak(aerson):
    print("{}이 {}로 말을 합니다.".format(person.name, person.language))
Human.speak = speak
speak(person1)  #서울시민이 한국어로 말을 합니다.
speak(person2)  #인도인이 English로 말을 합니다.
person1.speak() #서울시민이 한국어로 말을 합니다.
person2.speak() #인도인이 English로 말을 합니다.

#실습

class Car():
    '''자동차'''
taxi = Car()
taxi.name = '택시'
