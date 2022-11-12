import math

items=int(input("Enter number of items: "))
boxes=int(input("Enter number items per box: "))

answer = math.ceil(items/boxes)

print(f"For {items} items, packing {boxes} items in each box, you will need {answer} boxes.")