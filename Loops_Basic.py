#simple
dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
for breed in dog_breeds:
    print(breed)

#simple range
promise = "I will not chew gum in class"
for n in range(5):
  print(promise)

#infinite loops
#works
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
for student in students_period_A:
  students_period_B.append(student)
  print(student)
#but this is borked
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
for student in students_period_A:
  students_period_A.append(student)
  print(student)

#break
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmation'
for dog in dog_breeds_available_for_adoption:
  print (dog)
  if dog == dog_breed_I_want:
    print("They have the dog I want!")
    break

#continue
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
for age in ages:
  if age < 21:
    continue
  print(age)

#while loops (with pop)
all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []
while len(students_in_poetry) < 6:
  student = all_students.pop()
  students_in_poetry.append(student)
print(students_in_poetry)

#nested loops
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for location in sales_data:
  print(location)
  for sale in location:
    scoops_sold += sale
print(scoops_sold)

# list comprehensions, it's like loops in lists! 
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [height for height in heights if height > 161]
print(can_ride_coaster)

celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit = [temp * 9/5 + 32 for temp in celsius]
print(fahrenheit)

#review
single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []
for digit in single_digits:
  print(digit)
  sqr = digit ** 2
  squares.append(sqr)
print(squares)
cubes = [digit ** 3 for digit in single_digits]
print(cubes)
