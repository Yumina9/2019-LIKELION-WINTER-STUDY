wintable = {
    '가위':'보',
    '바위':'가위',
    '보':'바위'
}

def rsp(mine,yours):
    if mine == yours:
        return 'draw'
    elif wintable[mine] == yours:
        return 'win'
    else:
        return 'lose'

resule = rsp('가위', '바위')
print(result)

messages = {
    'win':'이겼다!',
    'draw':'비겼다',
    'lose':'졌다...'
}
print(result[messages])

#실습

days_in_month = {
    #여기에 코드를 완성해 보세요.
    '1월':31,
    '2월':28,
    '3월':31    
 }
print(days_in_month)

#            ↓ 이름표는 문자열 또는 숫자를 주로 사용하지만
dict = {     "이름표"    :    [1,2,3] }
#                           ↑ 값은 리스트를 포함해서 무엇이든 올 수 있습니다.
print( dict["이름표"] )

#딕셔너리 수정하기 실습

days_in_month = {"1월":31, "2월":28, "3월":31}
days_in_month["2월"] = 29
print(days_in_month)

days_in_month = {"1월":31, "2월":28, "3월":31,"-1월":97889789}
del(days_in_month["-1월"])
print(days_in_month)