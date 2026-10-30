#Exercise 1

"""Instructions:
1. Ask the user for two inputs:

A number (integer).
A length (integer).
2. Create a program that generates a list of multiples of the given number.
3. The list should stop when it reaches the length specified by the user.

Example 1:

Input:

number: 7
length: 5
Output:
[7, 14, 21, 28, 35]"""

number= int(input("Choose a number "))
lenght = int(input("Choose a different number "))
multiples = []
for i in range (1, lenght + 1):
    multiple = number * i
    multiples.append(multiple)
print(multiples)

#Exercise 2
"""instructions:
1. Ask the user for a string.
2. Write a program that processes the string to remove consecutive duplicate letters.

The new string should only contain unique consecutive letters.
For example, “ppoeemm” should become “poem” (removes consecutive duplicates like ‘pp’, ‘ee’, and ‘mm’).
3. The program should print the modified string.



Example 1:

Input:
user’s word: "ppoeemm"
Output:
"poem"""

word = input("Type a word")
word_fixed = ""
for letter in word:
    if not word_fixed or letter != word_fixed [-1]:
        word_fixed += letter
print(word_fixed)