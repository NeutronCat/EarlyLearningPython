#counts letters
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def unique_english_letters(word):
  uniques = 0
  for letter in letters:
    if letter in word:
      uniques += 1
  return uniques
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

def count_char_x(word, x):
  occurrences = 0
  for letter in word:
    if letter == x:
      occurrences += 1
  return occurrences
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

def count_multi_char_x(word, x):
  splits = word.split(x)
  return(len(splits)-1)
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

#slicing string using find
def substring_between_letters(word, start, end):
  start_ind = word.find(start)
  end_ind = word.find(end)
  if start_ind > -1 and end_ind > -1:
  	return(word[start_ind+1:end_ind])
  return word
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"

#word length
def x_length_words(sentence, x):
  words = sentence.split(" ")
  for word in words:
    if len(word) < x:
      return False
  return True
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True

#check for name
def check_for_name(sentence,name):
  if name.lower() in sentence.lower():
    return True
  else:
    return False 
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

#every other letter in word
def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 

#reverse_string, works because range takes start, end, step parameters and the -1 will count it down
def reverse_string(word):
  reverse = ""
  for i in range(len(word)-1, -1, -1):
    reverse += word[i]
  return reverse
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

#make spoonerism
def make_spoonerism(word1, word2):
  return word2[0]+word1[1:]+" "+word1[0]+word2[1:]
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a

#adding exclamations to 20
def add_exclamation(word):
  while(len(word) < 20):
    word += "!"
  return word
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))