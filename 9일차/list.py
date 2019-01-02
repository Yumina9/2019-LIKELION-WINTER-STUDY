list1 = {'가위', '바위', '보'}
list2 = {37, 23, 10, 33, 29, 40}

print(list1)
print(list2)

print(list1[1]) #바위
print(list1[2]) #보
print(list1[0]) #가위

list1[0] = '바위'
print(list1[0])
print(list1)

print(list1[-1]) #리스트의 가장 마지막 값
print(list1[-3])

#실습

rainbow=['빨강','주황','노랑','초록','파랑','남색','보라']
#rainbow를 이용해서 first_color에 값을 저장하세요
first_color = rainbow[0]
print('무지개의 첫번째 색은 {}이다'.format(first_color) )

rainbow=['빨강','주황','노랑','초록','파랑','남색','보라']
#rainbow를 이용해서 last_color에 값을 저장하세요
last_color = rainbow[-1]
print('무지개의 마지막 색은 {}이다'.format(last_color) )