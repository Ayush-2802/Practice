username = "ayushh"

def greet():
    print(f"Hello {username}") # This will print "Hello ayushh"
    username_local = "ayush" # This will create a new local variable username

print(username_local) # This will throw an error as username_local is not defined in the global scope

# To access the local variable username_local, we need to call the greet function
greet()
print(username_local) # This will throw an error as username_local is not defined in the global scope

# To access the global variable username, we can use the global keyword
def greet_global():
    global username
    print(f"Hello {username}") # This will print "Hello ayushh
    username = "ayush" # This will change the value of global variable username

greet_global()
print(username) # This will print "ayush"
    
