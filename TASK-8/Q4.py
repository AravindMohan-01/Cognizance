import pandas as pd
coll_name=pd.Series(['amrita', 'school', 'of', 'engineering' ,'chennai' , 'campus'])
print("Given Series :\n",coll_name)
cap_name=coll_name.str.capitalize()
print("\nAfter capitalizing : ",end="")
for i in range(len(cap_name)):
    print(cap_name[i],end=" ")
