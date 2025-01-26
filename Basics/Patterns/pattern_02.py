def numberCrown(n: int) -> None:
    # Write your solution here.
    space = 2*(n-1)
    for i in range(n):
        for j in range(1,i+2):
            print(j,end=" ")
            
        for k in range(1,space-(2*i)):
            print(" ",end="")
            
        for l in reversed(range(1,i+2)):
            print(l,end=" ")
        print()