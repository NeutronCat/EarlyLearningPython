#string slicing
first_name = "Reiko"
last_name = "Matsuki"
def password_generator(first_name,last_name):
  fnl = len(first_name)
  lnl = len(last_name)
  return first_name[fnl - 3:] + last_name[lnl - 3:]
temp_password = password_generator(first_name,last_name)

company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"
second_to_last = company_motto[-2]
final_word = company_motto[-4:]
print(final_word)

#immutable
first_name = "Bob"
last_name = "Daily"
#first_name[0] = "R" - this wont work because strings are immutable 
fixed_first_name = "R"+first_name[1:]
print(fixed_first_name)

# \ = escape character
password = "theycallme\"crazy\"91"

#iterating through string
def get_length(string):
  count = 0
  for letter in string:
    count += 1
  return count
print(get_length("chungus"))

def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  return False
print(letter_check("chungus","u"))

#conditionals in strings
def contains(big_string, little_string):
  return little_string in big_string
print(contains("chuffbox","chuff"))
def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common
print(common_letters("chuffbox","chuff"))

#review...
def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name  
def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password
print(username_generator("Bob","Cheeseman")) # BobChee
print(password_generator("BobChee")) # eBobChe

