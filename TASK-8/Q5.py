import numpy as np
print("2.Multiplying a matrix\n")
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("First Array :\n",A)
print("\nShape : ",A.shape)
B=np.identity(3,dtype=int)
print("\nSecond Array :\n",B)
print("\nShape : ",B.shape)
print("\n A X B = \n",np.matmul(A,B))

print("\n5.Re-Dimensioning an array")
bef_list=np.array([[1,2,3,4],[5,6,7,8]])
print("\nBefore Re-Dimensioning :\n",bef_list)
print("\nShape : ",bef_list.shape)
af_list=bef_list.reshape((4,2))
print("\nAfter Re-Dimensioning :\n",af_list)
print("\nShape : ",af_list.shape)

