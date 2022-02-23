print("Program to create a 2D list")
lr=4     #Number of rows
lc=3     #Number of columns
rows=[["Roll No","Name","Marks"]]
for i in range(lr-1):  #Creating and addings elements to the list
    columns=[] 
    for j in range(lc):
        if j==0:
            rollno=int(input("Enter the Roll No:"))
            columns.append(rollno)
        elif j==1:
            name=input("Enter the Name:")
            columns.append(name)
        else:
            mark=int(input("Enter the Mark:"))
            columns.append(mark)
    rows.append(columns)
print("\n")
print("i.Printing the list in tabular form")
for i in range(1):   #Printing the list
    for j in range(lc):
        print(rows[i][j],end=" ")
    print("\n")
for i in range(1,lr):   
    for j in range(lc):
        print(rows[i][j],end="\t")
    print("\n")
print("\n")
print("ii.Printing the second record")
for j in range(lc):
    print(rows[2][j],end=" ")
print("\n")
    
