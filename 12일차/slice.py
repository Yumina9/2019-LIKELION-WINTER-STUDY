list = ['영', '일', '이', '삼', '사', '오']
list[1:3]  #['일', '이']
list[1]  #'일'
list[3]  #'삼'
list[0:2] #['영','일']
list[2:len(list)]  #['이', '삼', '사', '오']
list[2]  #'이'
list[:2] #['영', '일']
list[2:] #['이', '삼', '사', '오']
list[:]  #['영', '일', '이', '삼', '사', '오']
list1=[2, 1, 3, 4]
list2=list1[:]
list1  #[2, 1, 3, 4]
list2  #[2, 1, 3, 4]
list1.sort()
list1  #[1, 2, 3, 4]
list2  #[2, 1, 3, 4]

#실습

rainbow = ["빨", "주", "노", "초", "파", "남", "보"]
# red_colors가 ["빨", "주", "노"]의 값을 가지도록 rainbow를 slice하세요.
red_colors = rainbow[:3]
#blue_colors가 ["파", "남", "보"]의 값을 가지도록 rainbow를 slice하세요.
blue_colors = rainbow[4:]
print("red_colors의 값 : {}".format(red_colors))
print("blue_colors의 값 : {}".format(blue_colors))

def substring(text, start, end):
    return text[start:end]
my_text = "Hello world"
between_2_5 = substring(my_text, 2, 5)
print(between_2_5)