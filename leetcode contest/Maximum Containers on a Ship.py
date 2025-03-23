def MaximumContainersonaShipBrute(n,w,m):
    c = 0
    for i in range(1,(n*n)+1):
        if w*i <= m:
            c += 1
    return c

def MaximumContainersonaShipOptimal(n,w,m):
    return min (n*n,m//w)

