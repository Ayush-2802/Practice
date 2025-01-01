lst = ['Chole Bhature', 'Rajma Chawal', 'Pav Bhaji', 'Dosa', 'Poha']
print(lst)
print(lst[0])
print(lst[1])

lst[3] = 'Idli'
print(lst) # value changes from Dosa to Idli

lstcopy = lst # both lst and lstcopy point to the same list
lstcopy = lst.copy() # lstcopy is a new list with same elements as lst