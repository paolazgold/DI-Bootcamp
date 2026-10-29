###Instructions 
# Exercise 1 - Print the following output using one line of code:
"""Hello world
Hello world
Hello world
Hello world"""

print("Hello world"*4) #Didnt work because they are together
print ("Hello world\n"*4)



#Exercise 2: Some Math
"""Instructions
Write code that calculates the result of:

(99^3)*8 (meaning 99 to the power of 3, times 8)."""

print((99**3)*8)

#Exercise 3:
print(5 < 3) #False
print(3 == 3) #True
print(3 == "3") #False
#print("3" > 3) #False #I left this sentence as comment, otherwise, shows me error in other exercises.
print("Hello" == "hello") #False

#Exercise 4:

"""Create a variable called computer_brand which value is the brand name of your computer.
Using the computer_brand variable, print a sentence that states the following:
"I have a <computer_brand> computer."""

computer_brand = "Mac"
print(f"I have a {computer_brand} computer.")

#Exercise 5:
"""Instructions
Create a variable called name, and set it’s value to your name.
Create a variable called age, and set it’s value to your age.
Create a variable called shoe_size, and set it’s value to your shoe size.
Create a variable called info and set it’s value to an interesting sentence about yourself. 
The sentence must contain all the variables created in parts 1, 2, and 3.
Have your code print the info message.
Run your code."""

name = "Paola"
age = 37
shoe_size = 37
info = f"My name is {name}, I am {age} old, my shoe size is {shoe_size} and I love ice cream"
print(info)

#Exercise 6:
"""Instructions
Create two variables, a and b.
Each variable’s value should be a number.
If a is bigger than b, have your code print "Hello World"."""

a=15
b=10

if a > b:
    print("Hello world!")

#Exercise 7:
"""Write code that asks the user for a number and determines whether this number is odd or even.


number = int(input("Type a number"))

if number % 2 == 0:
    print("This number is even")
else:
    print("This number is odd")""" #I changed this exercise to comment because it was affecting the exercise 8

    
#Exercise 8:
"""Write code that asks the user for their name and determines whether or not you have the same name. 
    Print out a funny message based on the outcome."""

"""user_name = input("What is your name: ")

if user_name =="Paola":
    print ("That is the best name")
else:
    print(f"Nice to meet you, {user_name}!")"""

    #Exercise 9 - Tall enough to ride a roller coaster

"""
Write code that will ask the user for their height in centimeters.
If they are over 145 cm, print a message that states they are tall enough to ride.
If they are not tall enough, print a message that says they need to grow some more to ride."""

roller_coaster_height = int(input("What is your height? Please answer in cm"))

if roller_coaster_height < 145:
    print("You still need to grow some cm to ride")
else:
    print("You are tall enough to ride!")