

a, b = 1, 2
a   #1
b   #2
c = (3, 4)
c  #(3, 4)
d, e = c
d  #3
e  #4
f = d, e
f  #(3, 4)
x=5
y=10
temp = x
x = y
y = temp
x  #10
y  #5
x,y = y,x
x  #5
y  #10
def tuple_func():
    return 1, 2
    
q,w = tuple_func()
q  #1
w  #2

#실습

x = 3
y = 5
position = x, y

a = 1
b = 2
#코드를 작성해 보세요.
a, b = b, a
print("a : {}, b : {}".format(a, b))
