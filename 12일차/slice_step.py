# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
list1 = list(range(20))
list1[5:15]  # [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
list1[5:15:2]  # [5, 7, 9, 11, 13]
list1[5:15:3]  # [5, 8, 11, 14]
list1[15:5:-1]  # [15, 14, 13, 12, 11, 10, 9, 8, 7, 6]
list1[::3]  # [0, 3, 6, 9, 12, 15, 18]
list1[::-3]  # [19, 16, 13, 10, 7, 4, 1]

# 실습

list1 = list(range(20))
# new_list가 5, 8, 11, 14의 값을 가지도록 list1을 slice하세요
new_list = list1[5:15:3]
print(new_list)
# reverse_list가 17, 13, 9, 5의 값을 가지도록 list1을 slice하세요
reverse_list = list1[17:4:-4]
print(reverse_list)
