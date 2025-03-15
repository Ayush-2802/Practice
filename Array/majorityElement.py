#brute  O(n^2)
def majorityElementbrute(arr,n):
    for i in range(n):
        c = 0
        for j in range(n):
            if arr[j] == arr[i]:
                c+=1
        if c > n/2 : return arr[i]

#better 
def majorityElementBetter(arr,n):
    d = {}

    for i in range(n):
        d[arr[i]] = d.setdefault(arr[i],0) + 1
    
    for k in d:
        if d[k] > n/2 :
            return k

def majorityElementOptimal(arr,n):
    ele = None
    c = 0

    for i in range(len(arr)):
        if c == 0:
            c = 1
            ele = arr[i]
        elif arr[i] == ele:
            c += 1
        else:
            c -= 1
    
    c1 = 0
    for i in range(n):
        if arr[i] == ele:
            c1 +=1
    
    if c1 > n/2:
        return ele
