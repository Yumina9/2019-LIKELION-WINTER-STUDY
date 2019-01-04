numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[0]
numbers  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[:5]  # [1, 2, 3, 4, 5]
del numbers[:5]  # [6, 7, 8, 9]
numbers[1:3] = [77, 88, 99]
numbers  # [6, 77, 88, 99, 9]
numbers[1:4] = [8]
numbers[6, 7, 8]

# 실습

list1 = [0, 1, 2, 3, 4, 5]
# list1의 1부터 3까지를 slice를 이용해서 각각 11, 22, 33으로 바꿔보세요.
# 바꾸고 나면 list1은 [0, 11, 22, 33, 4, 5]가 되어야 합니다.
list1[1:4] = [11, 22, 33]
list2 = [0, 1, 2, 3, 4, 5]
# list2의 1부터 3까지를 del과 slice를 이용해서 지워보세요
# 바꾸고 나면 list2은 [0, 4, 5]가 되어야 합니다.
del list2[1:4]
print("list1 : {}, list2 : {}".format(list1, list2))
