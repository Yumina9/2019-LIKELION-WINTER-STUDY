my_list = [1, 2, 3, 4, 5, 6]
str = "Hello World"
str[0]  # 'H'
str[1]  # 'e'
3 in my_list  # True
9 in my_list  # False
"H" in str  # True
"z" in str  # False
my_list.index(5)  # 4
str.index("r")  # 8
characters = list("abcdef")
characters  # ['a', 'b', 'c', 'd', 'e', 'f']
words = "Hello World는 프로그래밍을 배우기에 아주 좋은 사이트 입니다."
words_list = words.split()
words_list  # ['Hello', 'World는', '프로그래밍을', '배우기에', '아주', '좋은', '사이트', '입니다.']
time_str = "10:35:27"
time_list = time_str.split(":")
time_list  # ['10' '35' '27']
":".join(time_list)  # '10:35:27'
" ".join(words_list)  # 'Hello World는 프로그래밍을 배우기에 아주 좋은 사이트 입니다.'

# 실습

str = "오늘은 날씨가 흐림"
# split()을 이용해서 str을 공백으로 나눈 문자열을 words에 저장하세요
words = str.split()
# index()를 이용해서 "흐림"이 words의 몇번째에 있는지 찾고,
# position에 저장하세요.
position = words.index("흐림")
words[position] = "맑음"
# join()을 이용해서 words를 다시 문자열로 바꿔 new_str에 저장하세요.
# words를 문자열로 바꿀때는 공백 한 칸을 기준으로 붙이면 됩니다.
new_str = " ".join(words)
print(new_str)
