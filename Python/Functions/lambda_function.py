a = lambda x: a**3
print(a(3))

area = lambda x,y: l*w
l = 5
w = 10
print("Area of rectangle is", area(l,w))

factorial = lambda n : 1 if n == 0 or n == 1 else n*factorial(n-1)
fibo = lambda n : 0 if n==0 else 1 if n==1 or n==2 else fibo(n-1)+fibo(n-1)