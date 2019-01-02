#rep

list1 = [1, 2, 3, 4]
list1.append(5)
list1  #[1, 2, 3, 4, 5]
list1.remove(1)
list1  #[2, 3, 4, 5]
dict1 = {1:'one',2:'two'}
tuple1 = (1, 2, 3)
tuple1  #(1, 2, 3)
type(tuple1)  #<class 'tuple'>
tuple2 = 1, 2, 3
tuple2   #(1, 2, 3)
type(tuple2)  #<class 'tuple'>
list1 = [1, 2, 3]
tuple3 = tuple(list1)
tuple3  #(1, 2, 3)
tuple3[0]  #1
tuple3  #2
tuple3[0] = 5  #error
del tuple[3]   #error
tuple.pop(0)   #error

#실습

tuple1 = (1,2,3)
tuple2 = 1,2,3
list3 = [1,2,3]
tuple3 = tuple(list3)\
if tuple1 == tuple2 == tuple3:
    print("tuple1과 tuple2와 tuple3은 모두 같습니다.")

tuple1 = (11, 22, 33)
for i in range( len( tuple1) ):
    print( tuple1[i] )