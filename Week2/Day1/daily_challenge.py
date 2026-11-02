daily_challenge.py

MATRIX_STR = '''
7ir
Tsi
h!x
i #
sM 
$a 
#t%''' 

#Step 1: Transforming the String into a 2D List
matrix = []
for row in MATRIX_STR.strip().split("\n"):
    matrix.append(list(row))

print(matrix)

#Step 2: Processing Columns Neo reads the matrix column by column, from top to bottom, starting from the leftmost column. You’ll need to write code that iterates through the columns of your 2D list.Think about how you can access the elements of a 2D list by column.
for col in range(len(matrix[0])):
    for row in range(len(matrix)):
        print(matrix[row][col])

#Step 3: Filtering Alpha Characters: only select alpha characters (letters). For each character in a column, check if it’s an alpha character. If it is, add it to a temporary string. Think about how you can check if a character is an alphabet letter.
temporary_string = " "

for col in range (len(matrix[0])):
    for row in range(len(matrix)):
        char = matrix [row][col]
        
        if char.isalpha():
            temporary_string += char

print(temporary_string)

#Step 4: Replacing Symbols with Spaces. Replace every group of symbols (non-alpha characters) between two alpha characters with a space. After you have gathered the alpha characters, you will need to iterate through them, and where there are non alpha characters between them, you will insert a space. Think about how you can keep track of when you encounter an alphabet character, and when you encounter a non alphabet character.

decoded_message = " "
previous_was_symbol = False

for col in range (len(matrix[0])):
    for row in range(len(matrix)):
        code = matrix [row][col]
        
        if code.isalpha():
            if previous_was_symbol:
                decoded_message += " "
                
            decoded_message += code
            previous_was_symbol = False

        else:
            previous_was_symbol = True

#Step 5:
print(decoded_message)