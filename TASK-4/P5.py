nrow=5
space=2*nrow-2
for i in range(nrow):
    for j in range(space):
        print(end=" ")
    space=space-1
    for j in range(i+1):
        print("*", end=" ")
    print("\r")

