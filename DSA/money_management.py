n = int(input())
numbers = list(map(int, input().split()))

even_sum = 0
odd_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print(f"{even_sum},{odd_sum}")
