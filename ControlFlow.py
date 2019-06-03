# user check / if statements

def dave_check(user_name):
  if user_name == "Dave":
    return "Get off my computer Dave!"
  if user_name == "angela_catlady_87":
    return "I know it is you Dave! Go away!"
# Enter a user name here, make sure to make it a string
user_name = "angela_catlady_87"
print(dave_check(user_name))

# relational operators 

def greater_than(x,y):
  if x == y:
    return "These numbers are the same"
print(greater_than(-4,1))
def graduation_reqs(credits):
  if credits >= 120:
    return "You have enough credits to graduate!"
print(graduation_reqs(120))

def graduation_reqs(gpa,credits):
  if credits >= 120 and gpa >= 2.0 :
    return "You meet the requirements to graduate!"
print(graduation_reqs(2.0,120))

def graduation_mailer(gpa,credits):
  if credits >= 120 or gpa >= 2.0:
    return True

def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and (credits < 120):
    return "You do not have enough credits to graduate."
  if (gpa < 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  if (gpa < 2.0) and (credits < 120):
    return "You do not meet either requirement to graduate!"

def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  else:
    return "You do not meet the GPA or the credit requirement for graduation."

def grade_converter(gpa):
  if (gpa >= 4.0):
    grade = "A"
  elif (gpa >= 3.0):
    grade = "B"
  elif (gpa >= 2.0):
    grade = "C"
  elif (gpa >= 1.0):
    grade = "D"
  elif (gpa >= 0.0):
    grade = "F"
  return grade
print(grade_converter(3.1))

# try & except valueerror 
def raises_value_error():
  raise ValueError
try:
  raises_value_error()
except: print("You raised a ValueError!")

# final summary

def applicant_selector(gpa,ps_score,ec_count):
  if (gpa >= 3.0) and (ps_score >= 90) and (ec_count >= 3):
    return "This applicant should be accepted."
  elif (gpa >= 3.0) and (ps_score >= 90) and (ec_count < 3):
    return "This applicant should be given an in-person interview."
  else:
    return "This applicant should be rejected."

