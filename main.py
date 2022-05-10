# -----------------------------
# Program: Palindrome Checker
# Author: Joshue Garcia
# -----------------------------

# User input the word to check
word = str(input("Enter a word to check if it is a palindrome: "))

def palyndrome(s):
    # Remove spaces an turn the word into lowercase
    s = s.lower()
    s = s.replace(" ", "")
    
    # Takes first and last input
    left = 0
    right = len(s) - 1

    # Compare the first letter with the last letter.
    while left < right:
        # if letters not the same, the loop breaks else will compare the next letters
        if s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1
    return True


# Print the result

print(palyndrome('Anita lava la tina')) # True
print(palyndrome('Avengers Assemble')) # False
