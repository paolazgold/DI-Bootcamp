# Exercise 1: Favorite Numbers
"""Instructions:

Create a set called my_fav_numbers and populate it with your favorite numbers.
Add two new numbers to the set.
Remove the last number you added to the set.
Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
Note: Sets are unordered collections, so ensure no duplicate numbers are added."""

my_fav_numbers = {4, 24, 8}
my_fav_numbers.add(10)
my_fav_numbers.add(18)
my_fav_numbers.remove(18)

friend_fav_number = {30, 40, 50, 60}

our_fav_numbers = my_fav_numbers | friend_fav_number

print(our_fav_numbers)

#Exercise 2 - Tuple
"""Given a tuple of integers, try to add more integers to the tuple.
Hint: Tuples are immutable, meaning they cannot be changed after creation. 
Think about why you can’t add more integers to a tuple.
"""
"""tuple_exercise = (1,2,3)
tuple_exercise.add(4)

print(tuple_exercise)

tuple_exercise = tuple_exercise + (4,5,6)

print(tuple_exercise)"""

#Exercise 3

"""Key Python Topics:

List methods: append, remove, insert, count, clear


Instructions:

You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
Remove "Banana" from the list.
Remove "Blueberries" from the list.
Add "Kiwi" to the end of the list.
Add "Apples" to the beginning of the list.
Count how many times "Apples" appear in the list.
Empty the list.
Print the final state of the list."""

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0,"Apples")

print(basket.count("Apples"))
basket.clear()

print(basket)

#Exercise 4


"""Instructions:

Recap: What is a float? What’s the difference between a float and an integer?
Create a list containing the following sequence of mixed types: floats and integers:
1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
Avoid hard-coding each number manually.
Think: Can you generate this sequence using a loop or another method?"""

#1 Float is a number with decimal point

#2 We can create with while loop

list_float = []
number= 1.5

while number <= 5:
    list_float.append(number)
    number += 0.5

print(list_float)

#Exercise 5

"""Instructions:

Write a for loop to print all numbers from 1 to 20, inclusive.
Write another for loop that prints every number from 1 to 20 where the index is even."""

for loop_numbers in range (1,21):
    print(loop_numbers)

for loop_numbers in range (1,21):
    if loop_numbers % 2 == 0:
        print(loop_numbers)

#Exercise 6

"""Instructions: nstructions:

Use an input to ask the user to enter their name.
Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
hint: check for the method isdigit()
if the input is incorrect, keep asking for the correct input until it is correct
if the input is correct print “thank you” and break the loop"""

while True:
    user_name = input("What is your name? ")
    if len(user_name) >= 3 and not user_name.isdigit():
        print('Thank you')
        break

    else:
        print('That is not a correct, please type your name')

#Exercise 7

"""Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
Store these fruits in a list.
Ask the user to input the name of any fruit.
If the fruit is in their list of favorite fruits, print:
"You chose one of your favorite fruits! Enjoy!"
If not, print:
"You chose a new fruit. I hope you enjoy it!"
"""

fruits_list = input("Please tell me your all your favorite fruits, separeted by spaces: ").split()
fruit_item = input("Type a name of a fruit: ")
if fruit_item not in fruits_list:
    print("You chose a new fruit. I hope you enjoy it!")
else:
    print("You chose one of your favorite fruits! Enjoy!")

#Exercise 8

"""Write a loop that asks the user to enter pizza toppings one by one.
Stop the loop when the user types 'quit'.
For each topping entered, print:
"Adding [topping] to your pizza."
After exiting the loop, print all the toppings and the total cost of the pizza.
The base price is $10, and each topping adds $2.50."""


pizza_toppings = []
total_price = 10 + len(pizza_toppings)*2.5

while True:
    topping = input("What do you want in your pizza (type'quit' to finish)")
    if topping == "quit":
        break        
    pizza_toppings.append(topping)

    print(f"Adding {topping} to your pizza")

print(f"Your toppings are {pizza_toppings}")
print(f"The total price of your pizza is {total_price}")

#Exercise 9
"""Instructions:

Ask for the age of each person in a family who wants to buy a movie ticket.
Calculate the total cost based on the following rules:
Free for people under 3.
$10 for people aged 3 to 12.
$15 for anyone over 12.
Print the total ticket cost."""

total_price = 0

family_members = int(input("How many people are going to the movie? "))

for person in range(family_members):

    age = int(input('Enter the person age: '))

    if age < 3:
        total_price += 0

    elif age <=12:
        total_price +=10

    else:
        total_price +=15
    
    print(f"The total is ${total_price}")
