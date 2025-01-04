try:    
    number = int(input("Enter a number"))
    print(1/number)
except ZeroDivisionError:
    print("u cant divide by zero")
except ValueError:
    print("enter only numbers please!")
except Exception: #badPractice
    print("Something went wrong")
finally:
    print("restart or retry")


