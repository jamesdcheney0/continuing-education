inventory = {'rope':1, 'torch':6,'gold coin':42, 'dagger':1, 'arrow':12}

# for items in inventory
# print(value key)

def printInventory():
    print('Inventory:')
    # this works, and prints out the inventory dictionary in whatever order it wants
    # for i, v in inventory.items():
        # print(i + ': ' + str(v))
    # this prints out the inventory dictionary based on the highest value, going to the lowest 
    # from the second highest post on [this](https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value) stackoverflow question
    for w in sorted(inventory, key=inventory.get, reverse=True):
        print(w + ': ' +  str(inventory[w]))
    print('Total number of items: ' + str(sum(inventory.values())))

def addToInventory(inventory, addedItems):
    # for the key in dragon loot
    for key in dragonLoot:
    # if there is a matching key in inventory
        if key in inventory.keys():
    # then value += 1
            inventory[key] += 1
    else:
    # add key and value to inventory
        inventory[key] = 1
    # inventory.get(dragonLoot key, dragonLoot value)
    # for i, v in addedItems.items():
    #     inventory.get(i, v)
    #     print(inventory)
    # maybe range through the list to list out its contents, and add those to a dictionary. 
    # how in the world to increment a value in a dictionary if there are duplicate values
    # for v in range(len(dragonLoot)):
    #     inventory.get(dragonLoot[v],1)
    #     print(dragonLoot[v])
    # print(inventory)
    # copied from [this](https://www.reddit.com/r/learnpython/comments/ez7led/list_to_dictionary_function_for_fantasy_game/) guy's post 
    # this is basically what I wrote out at the top, just didn't know how to express it... 
    # I wrote it again at the top, between the phrases I originally said. I didn't know about assigning a value to a dictionary with `dictionary[key]=value`. Important piece of information
    # for item in dragonLoot:
    #     if item not in inventory.keys():
    #         inventory[item] = 1
    #     else: 
    #         inventory[item] += 1

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# inventory = addToInventory(inventory, dragonLoot)
addToInventory(inventory, dragonLoot)
printInventory()