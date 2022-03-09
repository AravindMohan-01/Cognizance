import numpy as np
list1=np.array([1,0,0,0,1,0])
print("First Array:",list1)
list2=np.array([0,0,1,1,0,1])
print("Second Array:",list2)
comp_list= list1==list2
equality=comp_list.all()
print(equality)
