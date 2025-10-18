age = int(input("Enter your age: "))  # Convert input to an integer

print("Welcome to our brand new cinema!")

if age <= 4:
    print("Your price is $5")
elif age <= 10:
    print("Your price is $10")
elif age <= 18:
    print("Your price is $15")
elif age <= 64:
    print("Your price is $20")
else:
    print("Your price is $0")
