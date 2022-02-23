num=int(input("Enter the number:"))
num1=num
rev=0
while num1>0:
    digit=num1%10
    rev=rev*10+digit
    num1=num1//10
if rev==num:
    print("True")
else:
    print("False")
