#write a generator function that yields the even numbers upto a specified limit

def even_numbers(limit):
    for i in range(2,limit+1,2):            
        yield i

limit = 10
for i in even_numbers(limit):
    print(i, end=" ") # 2 4 6 8 10