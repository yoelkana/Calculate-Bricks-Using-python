blocks = int(input("Enter the number of blocks: "))
number = 0
height = 0
while blocks > number:
    blocks -= number
    number += 1
    if blocks < number:
        break
    else:
        height += 1
print("The height of the pyramid:", height)
