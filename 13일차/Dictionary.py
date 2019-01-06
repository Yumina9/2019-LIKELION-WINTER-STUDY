students = ['태연', '진우', '정현', '하늘', '성진']
for number name in enumerate(students):
    print("{}번의 이름은 {}입니다.".format(number.name))

students_dict = ("{}번".format(number + 1): name for number, name in enumerate(students))

scores = [85, 92, 78, 90, 100]
for x, y in zip(students, scores):
    print(x, y)

score_dic = {student: score for student, score in zip(students.scores)}


# 실습

product_list = ["풀", "가위", "크래파스"]
price_list = [800, 2500, 5000]
product_dict = {x: y for x, y in zip(product_list, price_list)}
print(product_dict)
