# Question 2: Restaurant Order System (Lesson 2 - If/Elif/Else)
print("=== RESTAURANT MENU === \n 1. Pizza - $15.99 \n 2. Burger - $12.50 \n 3. Salad - $9.99 \n 4. Pasta - $13.75")

Choice = int(input("Enter your choice (1-4): "))
drink = input("Would you like a drink? ($2.50) (yes/no): ")
    # yes = "Drink: Yes - $2.50"
    # no = "Drink: No"
    # item = "Food:"
    

if Choice == 1 and drink == "yes":
        print("=== YOUR ORDER === \n Food: Pizza - $15.99 \n Drink: Yes - $2.50 \n Subtotal: $18.49 \n Tax (8%): $1.48 \n Total: $19.97")
        
#     elif Choice == 2:
#         print(f"{item} Burger - $12.50")
        
#     elif Choice == 3:
#         print(f"{item} Salad - $9.99")
        
#     elif Choice == 4:
#         print(f"{item} Pasta - $13.75")

#     else:
#         print("Invalid Response. Please use a number between 1-4.")

#     if drink == "yes":
#         print("Drink: Yes - $2.50")
        
#     elif drink == "no":
#         print("Drink: No $0")
        
# except ValueError:
#     print("Please enter valid numbers")
    
# if Choice == 1