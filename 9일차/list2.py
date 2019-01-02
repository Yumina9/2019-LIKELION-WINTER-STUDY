list2 = {37, 23, 10, 33, 29, 40}
print(list2)

#list2.append(16)
#print(list2)

list3 = list2 + [16]
print(list3)

list4 = list3 + list2
print(list4)

n = 12
ownership = n in list3
print(ownership)

n = 10
if n in list3:
    print('{}은 있어!'.format(n))

print(list4)
del list4[12]
print(list4)
list4.remove(40)
print(list4)

#실습

list1=[1,2,3]
#이 곳에 4를 추가하는 코드를 입력해 보세요.
list1 = list1 + [4]
print(list1)

list1=[1,2,3]
list2=[4,5,6]
list3 = list1 + list2
print(list3)

numbers = [1,2,3,4,5]
if 5 in numbers :
    print("5가 있다")

list1=[1,2,3]
# 여기에 코드를 추가해 보세요.
del list1[1]
print(list1)