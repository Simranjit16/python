#/usr/bin/python3
adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
p=[]
q=[]
print("Number greater than 5")
for i in adhoc:
 if i>5:
       print(i)
       p.append(i)
print("Number less then and equal to 2")
for i in adhoc:
 if i<=2:
       print(i)
       q.append(i)
print("list 1 is :",p)
print("list 2 is :",q)
