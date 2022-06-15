from services.speak import narrate

inventory = []
name = "greg"
health = 100
gold = 0


def obtainItem(item):
    narrate([f"you've obtained a {item}!"])
    global inventory
    inventory.append(item)
    print('  inventory: ', inventory)
    print("\n")


def reset():
    inventory = []
    health = 100
    gold = 0
