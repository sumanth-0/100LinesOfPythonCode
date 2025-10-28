import datetime
import time

# print(time.localtime())
# print(time.localtime().tm_mday)
# current_time = time.asctime()[11:19]

# print(time.time_ns())
print(datetime.time())

work_time = int(input("Enter work time in mins: "))
break_time = int(input("ENter break time in mins: "))


def work_func():
    delta = datetime.timedelta(minutes = work_time)
    second = datetime.timedelta(seconds = 30)
    current_time = datetime.datetime.now()
    start_time = current_time
    print(start_time)
    while True:
        if datetime.datetime.now() - current_time >= second:
            current_time = datetime.datetime.now()
            print(time.asctime())
            
        if datetime.datetime.now() - start_time >= delta:
            print("BREAK TIME")
            break_func()

def break_func():
    delta = datetime.timedelta(minutes = break_time)
    second = datetime.timedelta(seconds = 30)
    current_time = datetime.datetime.now()
    start_time = current_time
    print(start_time)
    while True:
        if datetime.datetime.now() - current_time >= second:
            current_time = datetime.datetime.now()
            print(time.asctime())
        if datetime.datetime.now() - start_time >= delta:
            print("BREAK TIME OVER")
            work_func()

work_func()


        
