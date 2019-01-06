import datetime
datetime.datetime.now() #datetime.datetime.now(년, 월, 일, 시, 분, 초, 마이크로초)
start_time = datetime.datetime.now()
type(start_time) #<class 'datetime.datetime'>
start_time.replace(year = 2017, month = 2, day = 1) #datetime.datetime(2017, 2, 1, 시, 분, 초, 마이크로초)
start_time = start_time.replace(year = 2017, month = 2, day = 1)
start_time #datetime.datetime(2017, 2, 1, 시, 분, 초, 마이크로초)
start_time = datetime.datetime(년도, 월, 일)
start_time #datetime.datetime(년도, 월,일,0, 0, 0, 0)
how_long = start_time - datetime.datetime.now()
type(how_long) #<class 'datetime.itmedelta'>
how_long.days  #9
how_long.seconds #33639
"2월 1일까지는 {}일 {}시간이 남았습니다".format(how_long.days, how_long.seconds//3600) #2월 1일까지는 9일 9시간이 남았습니다.

#실습

import datetime
christmas_2016 = datetime.datetime(2016, 12, 25)
print(christmas_2016)