ages = {'Tod':35, 'Jane':23, 'Pual':62}

for key, value in ages.items():
    print('{}의 나이는 {}입니다.'.format(key,value))

#실습

days_in_month = {"1월":31, "2월":28, "3월":31, "4월":30, "5월":31}
for key in days_in_month:
    print(key)
    
days_in_month = {"1월":31, "2월":28, "3월":31, "4월":30, "5월":31}
#출력 형식은 아래 print함수를 참고하세요
for key, value in days_in_month.items():
    print("{}은 {}일이 있습니다.".format( key, value  ) )