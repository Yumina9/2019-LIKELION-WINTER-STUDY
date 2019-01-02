#rep

list = [1, 2, 3, 4, 5]
dict = {'one':1, 'two':2}
list[0]      #1

dict['one']  #1

del(list[0])
list     #[2, 3, 4, 5]

del(dict['one'])
dict     #{'two': 2}

len(list)  #4
list   #[2, 3, 4, 5]

len(dict)  #1
dict  #{'two': 2}

list  #[2, 3, 4, 5]
2 in list  #True
7 in list  #False
'two' in dict.keys()  #True
'to' in dict.keys()   #False
2 in dict.values()    #True
32 in dict.values()   #False

dict.clear()
dict   #{}
list.clear()
list   #[]

list = [1, 2, 3, 4, 5]
dict = {'one':1, 'two':2}
list[2]   #3
list.pop(0)  #1
list  #[2, 3, 4, 5]
list[2]   #4
dict.pop('one')  #1
dict['two']    #2
big_list = [1, 2, 3]+[4, 5, 6]
big_list  #[1 , 2, 3, 4, 5, 6]
dict1 = (1:100,2:200)
dict2 = (1:1000,3:300)
dict1.update(dict2)
dict1    #(1:1000,2:200,3:300)
dict1 = (1:100,2:200)
dict = (1:1000,3:300)
dict2.update(dict1)
dict2     #(1:100,2:200,3:300)

#실습

def check_and_clear(box):
    if "불량품" in box.keys():
        box.clear()
        print("불량품이 있으면 box를 clear합니다.")
    else:
        print(box.keys())

products = {"풀":800, "딱풀":1200, "색종이":1000,"색연필":5000,"스케치북":3500}
catalog = {"겨울용 실내화":12000, "잠자리채":8000, "딱풀":1400}
products.update(catalog)