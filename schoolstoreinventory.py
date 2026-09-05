items= ["pencil","eraser","ruler","pen","calculator","highlighter"]
stocount=[33,23,13,35,0,15]

inventory= {item:count for item,count in zip(items,stocount)}
print(inventory)

in_stock_items=[item for item in items if inventory[item]>0]
print("Items in stock:", in_stock_items)

choseitem= input("Which Item Do You Want To Buy?")

if choseitem not in inventory or inventory[choseitem]==0:
    print(choseitem,"Oh No We Are Out Of Stock!")
    exit()

prices=[90,70,60,50,40,30]
markup=int(input("Enter the markup amount"))

marked_prices= list(map(lambda p: p+ markup,prices))
print(marked_prices)