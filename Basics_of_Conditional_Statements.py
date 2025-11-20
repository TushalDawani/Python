"""
age = 19
if(age >=18):
  print("You're Eligibile!")
else:
  print("You're not Eligible!")

"""

score = input("Enter your score: ")
score = float(score) # --> convert str to float (type casting.)


if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
