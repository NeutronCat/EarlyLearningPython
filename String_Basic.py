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

#string formatting
poem_title = "spring storm"
poem_author = "William Carlos Williams"
poem_title_fixed = poem_title.title()
print(poem_title_fixed)
poem_author_fixed = poem_author.upper()
print(poem_author_fixed)

#string splitting into lists
line_one = "The sky has given over"
line_one_words = line_one.split()
print(line_one_words)

authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"
author_names = authors.split(",")
print(author_names)
author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])
print(author_last_names)

spring_storm_text = \ # \n splits by new line, \t splits by tab
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""
spring_storm_lines = spring_storm_text.split("\n")
print(spring_storm_lines)

#joining list elements into strings, delimiter comes first
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = " ".join(reapers_line_one_words)
print(reapers_line_one)

#you can also use comma to make CSV lists, or escape sequences
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']
winter_trees_full = "\n".join(winter_trees_lines)
print(winter_trees_full)

#strip to remove whitespace, append and join
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']
love_maybe_lines_stripped = []
for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())
love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)

#replace
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""
toomer_bio_fixed = toomer_bio.replace("Tomer","Toomer")
print(toomer_bio_fixed)

#find, first index of character in string
god_wills_it_line_one = "The very earth will disown you"
disown_placement= god_wills_it_line_one.find("disown")
print(disown_placement)

#format, include variables in strings 
def poem_title_card(title,poet):
  output = """The poem "{}" is written by {}.""".format(title,poet)
  return output
print(poem_title_card("I hear America Singing", "Walt Whitman"))

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc
my_beard_description = poem_description(author = "Shel Silverstein",title = "My Beard", original_work = "Where the Sidewalk Ends", publishing_date = "1974")
print(my_beard_description)
