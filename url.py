#!/usr/bin/python3
from googlesearch import search
import time
# get the input from user to search a input
web=input("enter the topic ")
# know time to search
list1 = []
for i in search(web,stop=10):
	print(i) 
  # i print only url 
time.sleep(2)
list1.append(i)
print(list1)
f = open('url.txt','a+')
for i in list1:
	f.write(i+ '\n')
f.close()
