selected = None #아무 값도 들어있지 않다.
while selected not in ['가위', '바위', '보']:
    selected = input('가위, 바위, 보 중에 선택하세요>')

print('선택된 값은: ',selected)

patterns = ['가위', '보', '보']
length = len(patterns)
i=0
while i  < length:
    print(pattern[i])
    i=i+1

#실습

numbers = [1,2,3]
length = len(numbers)
i = 0
while i<length:
    print(numbers[i])
    i = i + 1
