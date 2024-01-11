

l1=[]


num1=int(input("enter a first number:"))
num2=int(input("enter a second no:"))

for i in range(1,min(num1,num2)):
    if num1 % i==0 and num2 %i ==0 :

        l1.append(i)
print(f"the gcd of two no is {max(l1)}")



 ## this is another method wich is direct function present in python ##
# from math import *
# a=math.gcd(14,63)
#
# print(a)
#
#
