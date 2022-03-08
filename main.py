# -----------------------------
# Program: Palindrome Checker
# Author: Joshue Garcia
# -----------------------------

# User input the word to check
word = str(input("Enter a word to check if it is a palindrome: "))

# Take the first index and the last index of the word
left_index = 0
right_index = len(word) - 1

# While loop to check if the word is a palindrome
while (left_index < right_index):
    # Convert the word to lowercase
    word = word.lower()
    palyndrome = True

    if word[left_index] != word[right_index]:
        palyndrome = False
        break
    else:
        left_index += 1
        right_index -= 1


# Print the result
print(palyndrome)
