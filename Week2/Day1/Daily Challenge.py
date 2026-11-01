"""Step 1: Transforming the String into a 2D List

Step 2: Processing Columns

Neo reads the matrix column by column, from top to bottom, starting from the leftmost column.
You’ll need to write code that iterates through the columns of your 2D list.
Think about how you can access the elements of a 2D list by column.

Step 3: Filtering Alpha Characters

only select alpha characters (letters).
For each character in a column, check if it’s an alpha character.
If it is, add it to a temporary string.
Think about how you can check if a character is an alphabet letter.

Step 4: Replacing Symbols with Spaces

Replace every group of symbols (non-alpha characters) between two alpha characters with a space.
After you have gathered the alpha characters, you will need to iterate through them, and where there are non alpha characters between them, you will insert a space.
Think about how you can keep track of when you encounter an alphabet character, and when you encounter a non alphabet character.


Step 5: Constructing the Secret Message
Combine the filtered and processed characters to form the decoded message.
Print the decoded message.


Example:



MATRIX_STR = '''
7ii
Tsx
h%?
i #
sM 
$a 
#t%''' 

# Step 1: Convert matrix_string to a 2D list (matrix)
matrix = []
# ... code to create matrix ...

# Step 2: Iterate through columns
# ... code to iterate through columns ...

# Step 3: Filter alpha characters
# ... code to filter alpha characters ...

# Step 4: Replace symbols with spaces
decoded_message = ""
# ... code to replace symbols with spaces ...

# Step 5: Print the decoded message
print(decoded_message)"""





MATRIX_STR = '''
7ii
Tsx
h%?
i #
sM 
$a 
#t%'''

matrix = [list(row) for row in MATRIX_STR.strip().split("\n")]

decoded_message = ""
previous_was_symbol = False

for col in range(len(matrix[0])):
    for row in range(len(matrix)):
        char = matrix[row][col]
        if char.isalpha():
            if previous_was_symbol and decoded_message:
                decoded_message += " "
            decoded_message += char
            previous_was_symbol = False
        else:
            previous_was_symbol = True

print(decoded_message)

