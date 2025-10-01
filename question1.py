# Question 1: Movie Ticket Pricing (Lesson 1 - Variables & Output)
name = input("What is your name? ")
age = int(input("What is your age? "))
quantity = input("How many tickets do you want to buy? 2")


child = 8
adult = 12
senior = 9



if age < 13 and age >= 1:
    print(f"\n === MOVIE TICKET RECEIPT === \n Customer: {name} \n Ticket Type: Child (${child}.00 each) \n Quantity: 2 \n Total Cost: (${child * 2}.00 each) \n Thank you for your purchase!")

elif  age >= 13 and age <= 64:
    print(f"\n === MOVIE TICKET RECEIPT === \n Customer: {name} \n Ticket Type: Adult (${adult}.00 each) \n Quantity: 2 \n Total Cost: (${adult * 2}.00 each) \n Thank you for your purchase!")
    
elif  age >= 65 and age <= 100:
    print(f"\n === MOVIE TICKET RECEIPT === \n Customer: {name} \n Ticket Type: Senior (${senior}.00 each) \n Quantity: 2 \n Total Cost: (${senior * 2}.00 each) \n Thank you for your purchase!")
    
else:
    print("\nNice Try. Please enter an age between 1 and 100.")
    