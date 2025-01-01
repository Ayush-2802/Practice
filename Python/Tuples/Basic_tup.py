#initialize a tuple
#tuple is immutable (value cant be assigned to be changed)
menu = ('Chole Bhature', 'Rajma Chawal', 'Pav Bhaji', 'Dosa', 'Poha')
print(menu)

#accessing elements of a tuple
print(menu[0])
print(menu[1])

#tuple concatenation
menu = menu + ('Idli', 'Sambhar')
print(menu)

#tuple repetition
menu = menu * 2
print(menu)

#count the number of times an element appears in a tuple
print(menu.count('Idli'))