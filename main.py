palabra = str(input())
palyndrome = True

# Take the First Index of the word
left_index = 0
# Take the Last Index of the word
rigth_index = len(palabra) - 1

while (left_index < rigth_index):
    if palabra[left_index] != palabra[rigth_index]:
        # if the word didn't match in both indexes it will not be a palyndrome
        palyndrome = False
        break
    else:
        # if both indexes match, the word will be cut while true
        left_index += 1
        rigth_index -= 1
    
print(palyndrome)