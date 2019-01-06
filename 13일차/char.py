s = "Hello world"
type(s)  #<class 'str>
f = 3.14
type(f)  #<class'float'>
i = 42
type(i)  #<class 'int'>
type(42.0)  #<class 'float'>
42 == 42.0  #True
isinstance(42, int)  #True
isinstance(42, float)  #False
isinstance(42.0, int)  #False
isinstance(42.0, float)  #True

#실습

my_list = [1, 2, 3]
my_dict = {"풀": 800, "색연필": 3000}
my_tuple = (1, 2, 3)
number = 10
real_number = 3.141592
print(type(my_list))
print(type(my_dict))
print(type(my_tuple))
print(type(number))
print(type(real_number))

