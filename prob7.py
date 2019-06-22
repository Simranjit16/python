#!/usr/bin/python3

# creating a new file

lc=input("enter the name of a file ")
file = open(lc,"w")

#creating multiple file togeather
num=int(input("enter a number of ew file you create")
for i in range(num):
	lc=input("enter name of a file ")
	myfile=open(lc,"w")
myfile.close()


#To cheack the access and modification time and update it
import os
lc=input("enter the location of file")
stinfo=os.stat(location)
print(stinfo)
print(os.utime(location,(stinfo.st_atime,stinfo.st_mtime)))
 
