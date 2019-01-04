list = [1, 2, 3, 5, 7, 2, 5, 237, 55]
for val in list:
    if val % 3 == 0:
        print(val)
        break  # 하나만 출력하고 싶을 때

for i in range(10):
    if i % 2 != 0:
        print(i0)
        print(i0)
        print(i0)
        print(i0)

for i in range(10):
    if i % 2 == 0:
        continue  # 제외해야 하는 경우를 첫번째 처리해줌으로 핵심이 되는 블록이 너무 깊게 들어가지 않도록 해준다.
        print(i)
        print(i)
        print(i)
        print(i)


# 실습

sizes = [33, 35, 34, 37, 32, 35, 39, 32, 35, 29]
for i, size in enumerate(sizes):
    if size == 32:
        print("사이즈 32인 바지는 {}번째에 있다.".format(i+1))
        break

numbers = [(1, 2), (10, 0)]
for a, b in numbers:
    if b == 0:
        print("0으로 나눌 수는 없습니다.")
        continue
    print("{}를 {}로 나누면 {}".format(a, b, a/b))
