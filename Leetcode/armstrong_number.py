num = int(input("Enter The number :"))
N = num
res = 0

while num :
    d = num % 10 
    num = num // 10
    res += d**3
   
if res == N:
    print("True")
else:
    print("False")