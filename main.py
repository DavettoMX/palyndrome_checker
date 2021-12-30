palabra = str(input())
palyndrome = True

# 
left_index = 0
rigth_index = len(palabra) - 1

while (left_index < rigth_index):
    if palabra[left_index] != palabra[rigth_index]:
        palyndrome = False
        break
    else:
        left_index += 1
        rigth_index -= 1
    
print(palyndrome)