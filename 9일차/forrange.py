
for i in range(5): # ~= [0, 1, 2, 3, 4]
    print(i)

names = {'정수', '영희' '바둑이', '귀보', '비단뱀'}

for i in range(len(names)):
    name = names[i]
    print('{}번: {}'.format(i+1, name))

for i, name in enumerate(names):
    print('{}번: {}'.format(i+1, name))

#for in list = 순화할 리스트가 정해져 있을 때
#for in range() = 순회할 횟수가 정해져 있을 때

#실습

for i in 
range(4):
    print(i)

rainbow=["빨","주","노","초","파","남","보"]
for i in range(len(rainbow)) :
    color = rainbow[i]
    print('{}번째 색은 {}'.format(i+1,color))

rainbow=["빨","주","노","초","파","남","보"]
for i,color in enumerate(rainbow) :
    print('{}번째 색은 {}'.format(i+1,color))

days = [31,29,31,30,31,30,31,31,30,31,30,31]
for i in range(len(days)) :
    day = days[i]
    print('{}월의 날짜수는 {}일 입니다.'.format( i+1 , day ))