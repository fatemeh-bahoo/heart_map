print("Welcome To Heart Map! \nYou can put the heart emoji where do you want!")
print('*Hint: You can use vertical and horizontal numbers like: "21" \nResult: ')

row4 = [" ⚪️ ", " ❤️  ", " ⚪️ "]
row5 = [" ⚪️ ", " ⚪️ ", " ⚪️ "]
row6 = [" ⚪️ ", " ⚪️ ", " ⚪️ "]

print(f"{row4}\n{row5}\n{row6}")

row1 = [" ⚪️ ", " ⚪️ ", " ⚪️ "]
row2 = [" ⚪️ ", " ⚪️ ", " ⚪️ "]
row3 = [" ⚪️ ", " ⚪️ ", " ⚪️ "]

map = [row1, row2, row3]

position = input("Now is your turn! Where do you want to put the heart emoji? ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = " ❤️  "

print(f"{row1}\n{row2}\n{row3}")