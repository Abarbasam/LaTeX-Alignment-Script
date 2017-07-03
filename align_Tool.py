import sys
from time import sleep

document = sys.argv[1] # The text file you want to align

# Counting how many lines are in the document
open_Doc = open(document, 'r')
num_Of_Lines = open_Doc.read().count("\n") # Counting the number of newlines
open_Doc.close()


# Re-opening the document so we can access individual lines
open_Doc = open(document, 'r')
document_Line = open_Doc.readlines()


whitespace_Lines = [0] # Marks each line where whitespace is detected
end_Block = False
num_Of_Rows = 0 # This later turns into the number of rows in a block 

for i in range(num_Of_Lines):
    if len(document_Line[i]) == 1: # If a blank line is found
        end_Block = True
        whitespace_Lines.append(i + 1) # This remembers where each line of whitespace is
    elif end_Block == False: #
        num_Of_Rows += 1


longest_Line_Memory = [] # Remembers the longest lines of each block
longest_Line = 0

# this block of code figures out the longest line in each block
for i in range(num_Of_Lines):
    if len(document_Line[i]) == 1: # If the block ends
        longest_Line_Memory.append(longest_Line) # Record the longest line of the block
        longest_Line = 0
    elif len(document_Line[i]) > longest_Line:
        longest_Line = len(document_Line[i])

longest_Line_Memory.append(longest_Line) # This makes sure that the last block also receives padding


padding_Counter = 0
stripped_Lines = [] # This will contain the stripped version of document_Line
formatted_Lines = [] # This will contain the contents of stripped_Lines, but with padding

# Strips the text document of newlines and trailing whitespace, and appends
# each new line into a list. Then, it formats each line into a another NEW list,
# where the new lines have padding
for i in range(num_Of_Lines):
    stripped_Lines.append(document_Line[i].rstrip()) # Getting rid of whitespace and newlines

for i in stripped_Lines:
    if i == '': # If a line with nothing in it is detected, you know you are done padding a block.
        padding_Counter += 1 # E.G. if longest_Line_Memory = [5, 6], then each item in the first block
                             # is given whitespace to make it 5 characters in length. Once an empty line is 
                             # detected, we know our block has ended, so we start padding
                             # the next block to be 6 characters in length. Each line in a given block is 
                             # padded the same amount, but each block usually has a different amount of padding.
    
    # Adds a certain amount of padding to each row, specific to each block
    formatted_Lines.append("{0:<{1}}".format(i, \
    (longest_Line_Memory[padding_Counter] + 3)))


out_Of_Range_Safeguard = 0 # Allows us to pop all useless ' ' items out of the list without using a for loop

while out_Of_Range_Safeguard < len(formatted_Lines):
    if formatted_Lines[out_Of_Range_Safeguard].isspace(): # If the item is only whitespace
        formatted_Lines.pop(out_Of_Range_Safeguard) # Get rid of it
    else:
        out_Of_Range_Safeguard += 1


block_Length = len(whitespace_Lines) # The amount of lines in a BLOCK
aligned_Lines = []

# This block rearranges the formatted lines to be in a side-by-side order
# and prints them
for i in range(num_Of_Rows):
    for j in range(block_Length):
        # Picks out the first item of each block and appends it to a list
        # Then, it picks the second item of each block and appends it to a list.
        # And so on and so on...
        aligned_Lines.append(formatted_Lines[i + (j * num_Of_Rows)])
        print aligned_Lines[j + (i * block_Length)],
    print
