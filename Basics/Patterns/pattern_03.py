def print_letter_pattern(rows):
    for i in range(rows):
        # Print spaces for centering
        print("  " * (rows - i - 1), end="")
        
        # Print first half of letters
        for j in range(i + 1):
            letter = chr(65 + j)
            print(letter, end=" ")
            
        # Print second half of letters (excluding the middle letter)
        for j in range(i - 1, -1, -1):
            letter = chr(65 + j)
            print(letter, end=" ")
            
        print()  # Move to next line

# Call the function with 3 rows
print_letter_pattern(3)
def print_alpha_triangle(n):
    for i in range(n):
        # Print spaces
        print(" " * (n - i - 1), end="")
        
        # Print letters in reverse order
        for j in range(i + 1):
            letter = chr(65 + (n - j - 1))
            print(letter, end=" ")
            
        print()  # Move to next line

print_alpha_triangle(3)