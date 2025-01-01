str = "123456789"

# Basic slicing
print("Full string:", str[:])        # 123456789
print("First 3:", str[0:3])          # 123
print("From 4th to end:", str[3:])   # 456789
print("Last 3:", str[-3:])           # 789
print("All except last 3:", str[:-3]) # 123456

# Using step
print("Every 2nd char:", str[::2])    # 13579
print("Every 3rd char:", str[::3])    # 147
print("Reverse string:", str[::-1])   # 987654321

# Slicing with negative indices
print("From -7 to -2:", str[-7:-2])   # 34567