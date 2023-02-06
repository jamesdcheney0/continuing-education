inventory = {'rope':1, 'torch':6,'gold coin':42, 'dagger':1, 'arrow':12}

# for items in inventory
# print(value key)

def printInventory():
    print('Inventory:')
    for i, v in inventory.items():
        print(v,i)
    print('Total number of items: ' + str(sum(inventory.values())))

def addToInventory(inventory, addedItems):
    # for the key in dragon loot
    # if there is a matching key in inventory
    # then value += 1
    # else:
    # add key and value to inventory
    # inventory.get(dragonLoot key, dragonLoot value)
    for i, v in addedItems.items():
        inventory.get(i, v)
        print(inventory)


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventory = addToInventory(inventory, dragonLoot)
printInventory()