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



