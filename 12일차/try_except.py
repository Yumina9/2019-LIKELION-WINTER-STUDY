text = '100%'
try:
    number = int(text)
except ValueError:
    print('{}는 숫자가 아니네요.'.format(text))  # 에러발생할경우 출력


def safe_pop_print(list, index):
    try:  # if index<len(list):
        print(list.pop(index))
    except IndexError:  # else:
        print('{} index의 값을 가져올 수 없습니다.'.format(index))


safe_pop_print([1, 2, 3], 5)

try:
    import my_module  # 에러가 발생할 가능성이 있는 코드
except ImportError:
    print("모듈이 없습니다.")  # 에러가 발생했을 경우 처리할 코드


# 실습

try:
    a = 3/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
