import numpy as np
org_list=np.array([10,11,12,13,14])
no_z=5
zero_list=np.zeros(len(org_list)+(len(org_list)-1)*(no_z))
zero_list[::no_z+1]=org_list
print(zero_list)
