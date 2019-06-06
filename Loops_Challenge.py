# loops challenge!

#count of nums divisible by ten
def divisible_by_ten(nums):
  count = 0
  for number in nums:
    if (number % 10 == 0):
      count += 1
  return count
print(divisible_by_ten([20, 25, 30, 35, 40]))

#Geetings
def add_greetings(names):
  greeting = []
  for name in names:
    greeting.append("Hello, "+name)
  return greeting
print(add_greetings(["Owen", "Max", "Sophie"]))

#delete starting even 
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

#odd indicies
def odd_indices(lst):
  oddlist = []
  for index in range(1, len(lst), 2):
    oddlist.append(lst[index])
  return oddlist
print(odd_indices([4, 3, 7, 10, 11, -2]))


