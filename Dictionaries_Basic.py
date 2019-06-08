#dictionaries 
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}
print(sensors)
print(num_cameras)

#    A dictionary begins and ends with curly braces ({ and }).
#    Each item consists of a key (i.e., “oatmeal”) and a value (i.e., 3)
#    Each key: value pair (i.e., "oatmeal": 3 or "avocado toast": 6) is separated by a comma (,)
#    It’s considered good practice to insert a space () after each comma, but your code will still run without the space.

# Dictionaries provide us with a way to map pieces of data to each other, so that we can quickly find values that are associated with one another.

# keys can be numbers as well

# Values can be any type. You can use a string, a number, a list, or even another dictionary as the value associated with a key!

translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}

#invalid keys

# We can have a list or a dictionary as a value of an item in a dictionary, but we cannot use these data types as keys of the dictionary. If we try to, we will get a TypeError.
# The word “unhashable” in this context means that this ‘list’ is an object that can be changed. Dictionaries in Python rely on each key having a hash value, a specific identifier for the key. If the key can change, that hash value would not be reliable. So the keys must always be unchangeable, hashable data types, like numbers or strings.
#wrong
#children = {["Johannes", "Rosmarie", "Eleonore"]: "von Trapp", ["Sonny", "Fredo", "Michael"]: "Corleone"}
#correct
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}

#  You can create an empty dictionary

my_empty_dictionary = {}

#adding keys to dictionary
animals_in_zoo = {}
animals_in_zoo['zebras'] = 8
animals_in_zoo['monkeys'] = 12
animals_in_zoo['dinosaurs'] = 0
print(animals_in_zoo)

# If we wanted to add multiple key : value pairs to a dictionary at once, we can use the .update() method

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

#overwrite values
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners.update({"Supporting Actress": "Viola Davis"})
oscar_winners["Best Picture"] = "Moonlight"
print(oscar_winners)

#List Comprehensions to Dictionaries
#Python allows you to create a dictionary using a list comprehension





