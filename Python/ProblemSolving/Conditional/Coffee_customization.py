ordersize = input("small, medium, or large? :").lower()
extra = input("Extra shot of espresso? :").lower()

if ordersize in ["small", "medium", "large"]:
    output = ordersize.capitalize() + " coffee"
    if extra == "yes":
        output += " with extra shot of espresso"
    print(output)
else:
    print("Invalid size")

