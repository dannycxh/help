#print("hellow world");

import urllib.request
import threading

page = urllib.request.urlopen("http://www.google.com").read()
print(page)



#Timer（定时器）是Thread的派生类，
#用于在指定时间后调用一个方法。

#
class Person(object):
    def __init__(self):
        print("init person")

    def speak(self):
        print("speak")


if (__name__ == "__main__"):
    logging.info("======== Here ==============")
    p = Person()
    while True:
        timer = threading.Timer(5, Person.speak, (p,))
        print("start")
        timer.start()
        timer.join()
        print("after join")