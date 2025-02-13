arr = list(map(int, input("Enter array elements separated by space: ").split()))
occ = int(input("Enter the number to find its occurance:"))

hash = [0]*len(arr)
for i in arr:
    hash[i] += 1

print(f"{occ} occured : {hash[occ]}")


class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr):
        n = len(arr)
        # Create hash array of size n to store frequencies of 1 to n
        hash = [0] * n
        
        # Count frequencies
        for i in range(n):
            if 1 <= arr[i] <= n:  # Only count elements in range 1 to n
                hash[arr[i]-1] += 1  # Subtract 1 since array is 0-indexed
        
        return hash

# Driver Code
if __name__ == "__main__":
    t = int(input())  # number of test cases
    for _ in range(t):
        arr = list(map(int, input().split()))  # input array
        s = Solution().frequencyCount(arr)  # find the frequencies
        
        # Output formatting
        if s:
            print(" ".join(map(str, s)))  # Print the result
        else:
            print("[]")  # Print empty list if no valid frequencies


