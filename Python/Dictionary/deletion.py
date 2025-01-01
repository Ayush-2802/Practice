menu = {'CholeBhature': 100,'PavBhaji': 120,'PaniPuri': 50, 'Dosa': 80}

# Deleting key-value pair
del menu['PavBhaji']
print(menu) #removes key-value pair from memory refrence

menu.pop('Dosa')
print(menu)
menu.popitem()
print(menu) #removes last key-value pair
menu.clear()
print(menu) #removes all key-value pairs    
