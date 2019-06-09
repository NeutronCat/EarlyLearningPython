#classes 
class Facade:
  pass # We used the pass keyword in Python to indicate that the body of the class was intentionally left blank so we don’t cause an IndentationError
  
# A class doesn’t accomplish anything simply by being defined. A class must be instantiated. 
  class Facade:
  pass
facade_1 = Facade()

# A class instance is also called an object. The pattern of defining classes and creating objects to represent the responsibilities of a program is known as Object Oriented Programming or OOP.
# Instantiation takes a class and turns it into an object, the type() function does the opposite of that. When called with an object, it returns the class that the object is an instance of.
# In Python __main__ means “this current file that we’re running” and so one could read the output from type() to mean “the class CoolClass that was defined here, in the script you’re currently running.”
class Facade:
  pass

facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type) # <class '__main__.Facade'>

# When we want the same data to be available to every instance of a class we use a class variable. A class variable is a variable that’s the same for every instance of the class.
# You can define a class variable by including it in the indented part of your class definition, and you can access all of an object’s class variables with object.variable syntax.
class Grade:
  minimum_passing = 65
 
# Methods are functions that are defined as part of a class
class Rules:
 def washing_brushes(self):
   return "Point bristles towards the basin while washing your brushes."
	
#Methods with Arguments




