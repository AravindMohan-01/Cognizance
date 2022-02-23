num=input("Enter the number:")
invnum=""
for i in range(len(num)-1,-1,-1):
    invnum=invnum+num[i]
if invnum==num:
    print("True")
else:
    print("False")
