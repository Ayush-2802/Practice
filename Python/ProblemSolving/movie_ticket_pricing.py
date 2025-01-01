age = int(input("Enter your age: "))
day = input("Enter the day: ")

if age<18:
    if day == "Wednesday":
        print("Ticket price is $6.00")
    else:
        print("Ticket price is $8.00")
else:
    if day == "Wednesday":
        print("Ticket price is $8.00")
    else:
        print("Ticket price is $10.00")