import time

print('''  
    _____________  ___    __
   /  _/  _/  _/ |/ / |  / /
   / / / / / / |   /| | / / 
 _/ /_/ /_/ / /   | | |/ /  
/___/___/___//_/|_| |___/   

Inventory Calculator By IIIXV#5945
                           ''')
time.sleep(2)


# Slots of the inventory
hbar = 9 
inv = 27 

# Question
hotbar = int(input('How many items are in your hot bar?\n'))

# If that's higher then do this
if hotbar > hbar:
    print('Sorry but you can only have 9 items in your hotbar. Please try again')
    time.sleep(2)
    hotbar = int(input('How many items are in your hot bar?\n'))

inventory = int(input('How many items are in your inventory?\n'))

if inventory > inv:
    print("Sorry but you've only gotten 27 slots in your inventory please, try agian")
    time.sleep(2)
    inventory = int(input('How many items are in your inventory?\n'))

v1 = hbar - hotbar
v2 = inv - inventory
v3 = v2 + v1

print(f"Hotbar Slots - {v1}")
print(f"Inventory Slots - {v2}")
print(f"Total Slots - {v3}")

farm = input("What are you farming? [e.g: Ender Pearls, Blaze Powder, Endstone, Cobblestone etc.]\n")

if farm in ('ender pearl', 'e pearl', 'enderpearl', 'epearl'):
    print(f"When you fill your inventory you will have - {v1 + v2 * 16} {farm}")
elif farm in ('eggs', 'egg'):
    print(f"When you fill your inventory you will have - {v1 + v2 * 16} {farm}")
elif farm in ('snowball', 'snow ball', 'snowballs', 'snow balls'):
    print(f"When you fill your inventory you will have - {v1 + v2 * 16} {farm}")
else:
    print(f"When you fill your inventory you will have - {v1 + v2 * 64} {farm}")
time.sleep(2)

input('Press enter to exit')
exit()