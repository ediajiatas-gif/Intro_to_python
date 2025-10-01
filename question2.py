# Question 2: Restaurant Order System (Lesson 2 - If/Elif/Else)
print("=== RESTAURANT MENU === \n 1. Pizza - $15.99 \n 2. Burger - $12.50 \n 3. Salad - $9.99 \n 4. Pasta - $13.75")

choice = int(input("Enter your choice (1-4): "))
drink_choice = input("Would you like a drink? ($2.50) (yes/no): ")

pizza = 15.99
burger = 12.50
salad = 9.99
pasta = 13.75

yes_drink = 2.50
no_drink = 0

if choice == 1:
    food_price = pizza
    print(f"Pizza - ${pizza}")
    
elif choice == 2:
    food_price = burger
    print(f"Burger - ${burger}")
    
elif choice == 3:
    food_price = salad
    print(f"Salad - ${salad}")

elif choice == 4:
    food_price = pasta
    print(f"Pasta: - ${pasta}")
    
if drink_choice == "yes":
    drink_price = yes_drink
    print(f"Drink: Yes - ${yes_drink}")

elif drink_choice == "no":
    drink_price = no_drink
    print(f"Drink: No - ${no_drink}")
    
subtotal = food_price + drink_price
print(f"Subtotal: ${subtotal:.2f}")
    
tax = subtotal * .08
print(f"Tax (8%): ${tax:.2f}")

total = subtotal + tax
print(f"Total: ${total:.2f}")