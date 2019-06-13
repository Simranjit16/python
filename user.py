#!/usr/bin/python3
import os
user=input("enter user name")
check=0
num={1,2,3,4,5,6,7,8,9,0}
for i in user:
  if i in str(num):
    check=1
if check == 1 :
      print("invalid user name")
else:
  psswd="hello"+user
  os.system("useradd -p"+psswd+" "+user)
print("you are successfully aded a new user")

