list = [1, 2, 3, 4, 5]
for a in enumerate(list):
    print('{}번째 값: {}'.format(*a))

ages = {'Tod':35,'Jane':23,'Paul':62}
for key,vaal in ages.items():
    print('{}의 나이는:{}'.format(*a))

#실습

products = {"풀" : 800, "색종이": 1000}
for product_detail in products.items():
    print("{}의 가격: {}원".format( *product_detail))
