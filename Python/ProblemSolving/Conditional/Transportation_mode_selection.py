distance = int(input("Enter the distance in Km: "))

if distance < 3:
    print("Walking")
elif distance < 15:
    print("Biking")
elif distance < 50:
    print("Car")
