from UnexpectedRSPValue import UnexpectedRSPValue.

value = '가'
try:
    if value not in ['가위', '바위', '보']:
        raise UnexpectedRSPValue("가위바위보 중에 하나의 값이어야 합니다.")
except UnexpectedRSPValue:
    print("에러가 발생했습니다.")


def sign_up():
    # 회원가입 함수


try:
    sign_up()
except BanUserName:
    print("이름으로 사용할 수 없는 입력입니다.")
except PasswrodNotMatched:
    print("입력한 패스워드가 서로 일치하지 않습니다.")

# 실습

# 이 아래에 Exception을 상속 받는 MyException클래스를 정의하세요.


class MyException(Exception):
    pass


shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}

try:
    for shop, products in shops.items():
        for product, price in products.items():
            if product == '풀':
                print("{}: {}원".format(shop, price))
                raise MyException
except MyException:
    print("풀을 찾았습니다.")
