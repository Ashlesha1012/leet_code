# from threading import *
# def name():
#     for i in range(1, 10):
#         print("Child Thread 1")
# t = Thread(target=name)
# t.start()
# for i in range(3, 5):
#     print("Main Thread ")

# class MyThread(Thread):
#     def run(self):                             #we have to override run method
#         for i in range(2, 9):
#             print("Child Thread")
# t = MyThread()
# t.start()
# for i in range(2, 5):
#     print("Main Thread")


# class MyThread:
#     def display(self):
#         for i in range(2, 9):
#             print("Child Class")
# obj = MyThread()
# t = Thread(target = obj.display)
# t.start()
# for i in range(2, 5):
#     print("Main Thread")


# import time
# def doubles(num):
#     for n in num:
#         time.sleep(1)
#         print("Doubles :", 2*n)
# def squares(num):
#     for n in num:
#         time.sleep(1)
#         print("Squares :", n*n)
# num = [1, 2, 3, 4, 5]
# begintime = time.time()
# doubles(num)
# squares(num)
# print("Total time taken", time.time()-begintime)

# from threading import *
# import time
# def doubles(num):
#     for n in num:
#         time.sleep(1)
#         print("Doubles :", 2*n)
# def squares(num):
#     for n in num:
#         time.sleep(1)
#         print("Squares :", n*n)
# num = [1, 2, 3, 4, 5]
# begintime = time.time()
# t1 = Thread(target=doubles, args=(num,))
# t2 = Thread(target=squares, args=(num,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("Total time taken", time.time()-begintime)


# from threading import *
# print(current_thread().name)
# current_thread().setName("Ashlesha")
# print(current_thread().getName())
# print(current_thread().name)


# from threading import *
# def dispaly():
#     print("Child Thread")
# t = Thread(target=dispaly)
# t.start()
# print("Current thread identity :", current_thread().ident)
# print("Child Thread identity :",t.ident)


# import time
# from threading import *
# def test():
#     print(current_thread().getName(),"...started")
#     time.sleep(7)
#     print(current_thread().getName(),"...ended")
# print("The no. of active threads : ", active_count())
# t1 = Thread(target=test, name="ChildThread1")
# t2 = Thread(target=test, name="ChildThread2")
# t3 = Thread(target=test, name="ChildThread3")
# t1.start()
# t2.start()
# t3.start()
# # t1.join()
# # t2.join()
# # t3.join()
# print("The no. of active threads : ", active_count())
# time.sleep(5)
# print("The no. of active threads : ", active_count())


# import time
# from threading import *
# def test():
#     print(current_thread().getName(),"...started")
#     time.sleep(3)
#     print(current_thread().getName(),"....ended")
# t1 = Thread(target=test, name="Child Thread 1")
# t2 = Thread(target=test, name="Child Thread 2")
# t3 = Thread(target=test, name="Child Thread 3")
# t1.start()
# t2.start()
# t3.start()
# l = enumerate()
# for t in l:
#     print(t.name)
# time.sleep(5)
# l = enumerate()
# for t in l:
#     print(t.name)


import time
from threading import *
def test():
    print(current_thread().getName(),"...started")
    time.sleep(4)
    print(current_thread().getName(),"....ended")
t1 = Thread(target=test, name="Child Thread 1")
t2 = Thread(target=test, name="Child Thread 2")
t3 = Thread(target=test, name="Child Thread 3")
t1.start()
t2.start()
t3.start()
print(t1.name, t1.is_alive())
print(t1.name, t2.is_alive())
print(t1.name, t3.is_alive())
time.sleep(5)
print(t1.name, t1.is_alive())
print(t1.name, t2.is_alive())
print(t1.name, t3.is_alive())
