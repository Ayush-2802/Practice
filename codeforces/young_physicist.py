n = int(input())
xi=yi=zi=0
for i in range(n):
    x,y,z = map(int,input().split())
    xi +=x
    yi +=y
    zi +=z

if xi == 0 and yi == 0 and zi == 0:
    print("YES")
else:
    print("NO")