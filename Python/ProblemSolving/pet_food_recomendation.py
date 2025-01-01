pet = input("Enter the type of pet: ").lower()
age = int(input("Enter the age of the pet: "))

pet_types = {
    "dog": "Puppy",
    "cat": "Kitten"
}

if pet in pet_types:
    if age < 2:
        print(f"{pet_types[pet]} food")
    elif age < 7:
        print("Adult food")
    else:
        print("Senior food")
