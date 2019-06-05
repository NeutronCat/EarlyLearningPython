#doubles the indexed list element
def double_index(lst, index):
  if index < len(lst):
  	lst[index] = lst[index] * 2
  return lst
print(double_index([3, 8, -10, 12], 2))

#removes middle of list
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

#more than n
def more_than_n(lst,item,n):
  if (lst.count(item) > n):
    return True
  else:
    return False
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

#more frequent items
def more_frequent_item(lst,item1,item2):
  if (lst.count(item2)) > (lst.count(item1)):
    return item2
  else:
    return item1
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

#produces middle or middle two elements of list
def middle_element(lst):
  if len(lst) % 2 == 0:
    mids = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return mids / 2
  else:
    return lst[int(len(lst)/2)]
print(middle_element([5, 2, -10, -4, 4, 5]))

#append sum
def append_sum(lst):
  apnd1 = ((lst[-1]) + (lst[-2]))
  lst.append(apnd1)
  apnd2 = ((lst[-1]) + (lst[-2]))
  lst.append(apnd2)
  apnd3 = ((lst[-1]) + (lst[-2]))
  lst.append(apnd3)
  return lst
print(append_sum([1, 1, 2]))

#Larger List
def larger_list(lst1,lst2):
  if len(lst2) > len(lst1):
    return lst2[-1]
  else:
    return lst1[-1]
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

#Combine Sort
def combine_sort(lst1,lst2):
  nulst = sorted(lst1 + lst2)
  return nulst
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

#Append Size
def append_size(lst):
  size = len(lst)
  lst.append(size)
  return lst
print(append_size([23, 42, 108]))

#Write your function here
def every_three_nums(start):
  return list(range(start,101,3)) 
print(every_three_nums(91))
