#!/usr/bin/python3
 # for cat command
file=open("file.txt","r")
print(file.read())



#for cat - E command 
for line in file:
        print(line.strip() + "$")

#foer cat -n command
fname=input("enter file name: ")  #take a input from user
num_lines = 0
with open(fname,'r') as f:
        for line in f:
                num_lines+= 1
print("number of lines :")
print(num_lines)

#for cat -s command
myfile=input("enter the input")
fh = open("myfile","r")  #read line as a list

