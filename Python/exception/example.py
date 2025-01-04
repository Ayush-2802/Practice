try:
    n = int(input("Enter a number to divide:"))
    d = int(input("Enter a number to divide by:"))
    res = n / d
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
except TypeError as e :
    print(e)
except Exception:
    print("something went wrong")
else:
    print(res)
finally:
    print("this will always execute")