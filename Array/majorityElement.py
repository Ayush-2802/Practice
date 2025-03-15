#brute
def majorityElementbrute(arr,n):
    for i in range(n):
        c = 0
        for j in range(n):
            if arr[j] == arr[i]:
                c+=1
        if c > n/2 : return arr[i]

#better
def majorityElementBetter(arr,n):
    pass