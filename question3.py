# Question 3: Pet Age Calculator 
while True:
    pet = input("Enter pet type (dog/cat/bird/hamster): ").lower()
    if pet in ["dog", "cat", "bird", "hamster"]:
        break
    else: 
        print("Invalid pet type. Please enter dog, cat, bird, or hamster")

while True:
    human_age = int(input("Enter your pet's age in human years: "))
    if human_age < 0:
        print("Age cannot be negative! Please enter a valid number.")
    else:
        break


print("=== PET AGE CONVERSION ===")
print(f"Pet Type: {pet}")
print(f"Human Age: {human_age} years")

if pet == "dog" or pet == "cat":
    if human_age <= 2:
        pet_age = 24
    else:
        pet_age = 24 + (human_age -2) * 4
    
elif pet == "bird":
    pet_age = human_age * 9
    
elif pet == "hamster":
    pet_age = human_age * 25
    
else:
    pet_age = None
    
if pet_age is not None:
    print(f"Pet Age: {pet_age} years")
    print(f"Fun Fact: Your {pet} is like a {pet_age} year-old human!")
    