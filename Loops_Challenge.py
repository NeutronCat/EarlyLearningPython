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

#nested base exponent loop
def exponents(bases, powers):
  new_lst = []
  for base in bases:
    for power in powers:
      new_lst.append(base ** power)
  return new_lst
print(exponents([2, 3, 4], [1, 2, 3]))

#larger sum of two lists
def larger_sum(lst1,lst2):
  cnt1 = 0
  cnt2 = 0
  for num in lst1:
    cnt1 += num
  for num in lst2:
    cnt2 += num
  if cnt1 >= cnt2:
    return lst1
  else:
    return lst2
print(larger_sum([1, 9, 5], [2, 3, 7]))

#over 9000!!!
def over_nine_thousand(lst):
  total = 0
  for number in lst:
    total += number
    if (total > 9000):
      break
  return total
print(over_nine_thousand([8000, 900, 120, 5000]))

#max num
def max_num(nums):
  maximum = nums[0]
  for num in nums:
    if num > maximum:
      maximum = num
    else:
      continue
  return maximum
print(max_num([50, -10, 0, 75, 20]))

#same values
def same_values(lst1, lst2):
  newlist = []
  for index in range(len(lst1):
    if lst1[index] == lst2[index]:
      newlist.append(lst1[index])
  return newlist
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

#reversed list
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))


