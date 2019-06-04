# learning lists in Python3

# basic lists
ints_and_strings = [1, 2, 3, 'four', 'five', 'chungus']
sam_height = ['Sam', 67]

#lists of lists
heights = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64], ['Vik', 68]]
ages = [['Aaron', 15], ['Dhruti', 16]]

# zip, creates list of pairs
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']
names_and_dogs_names = zip(names, dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)

# growing a list, Append, Plus
orders = ['daisies', 'periwinkle']
print(orders)
orders.append('tulips')
orders.append('roses')
print(orders)
new_orders = orders + ['lilac', 'iris']
prices = [5, 3, 4, 5, 4] + [4]

# Range
list1 = range(9) # 0 to 8
range1 = range(8) # 0 to 7
list1 = range(5, 15, 3)
list2 = range(0,40,5)

# summary
first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']
age = []
age.append(42)
all_ages = age + [32, 41, 29]
name_and_age = zip(first_names,all_ages)
ids = range(4)

#length, index, select via index
list1 = range(2, 20, 3)
list1_len = len(list1)
print(list1_len)

employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']
index4 = 'Ryan'
print(len(employees))
print(employees[4])

shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']
print(len(shopping_list))
last_element = (shopping_list[-1])
element5 = shopping_list[5]
print((shopping_list[-1]),(shopping_list[5]))

suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

beginning = suitcase[0:4]
print(beginning)
middle = suitcase[2:4]
print(middle)