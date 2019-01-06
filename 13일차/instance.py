type(5)  # <class 'int'>
isinstance(5, float)  # False
numbers1 = []  # <class 'list'>
numbers2 = list(range(10))
numbers2  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
chracters  # ['h', 'e', 'l', 'l', 'o']
type(numbers2)  # <class 'list'>
type(chracters)  # <class 'list'>
isinstance(numbers1, list)  # True
numbers1 == list  # False

# 실습

list1 = [1, 2, 3]
list2 = [1, 2, 3]

if list1 is list1:
    print("당연히 list1과 list1은 같은 인스턴스입니다.")
if list1 == list2:
    print("list1과 list2의 값은 같습니다.")
    if list1 is list2:
        print("그리고 list1과 list2는 같은 인스턴스입니다.")
    else:
        print("하지만 list1과 list2는 다른 인스턴스입니다.")

list1 = list(range(10))
list2 = [1, 2, 3]
if isinstance(list1, list) and isinstance(list2, list):
    print("list1과 list2는 둘 다 list클래스 입니다.")
