#creating Dictionary 
menu = {'CHoleBhature': 100,'PavBhaji': 120,'PaniPuri': 50, 'Dosa': 80}
print(menu)
print(menu['CHoleBhature']) #accessing value of key
print(menu.get('PavBhaji')) #get method is used to get value of key
print(menu.get('Lassi', 'Item not available')) #if key is not present in dictionary then it will return default value

#finding key in dictionary
if 'PavBhaji' in menu:
    print('PavBhaji is present in menu')
else:
    print('PavBhaji is not present in menu')

print(len(menu)) #length of dictionary

menucopy = menu.copy() #copying dictionary
print(menucopy)