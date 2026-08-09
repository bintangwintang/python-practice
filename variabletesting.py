"""
x = "John"
y = 67

print(x)
print(y)

print(type(x))
print(type(y))
"""

#personal stats example
#name, age, height, weight, ethnicity, occupation = "Rio", 32, "5'5", 110, "Japanese", "Actress"
#print("My name is",name,"and I am",age,"years old. I am",height,"tall and weigh",weight,"pounds. I am",ethnicity,"and I work as a",occupation,".")

#stats example 2 - USING LISTS / TUPLE
"""
stats = ("Rio", 32, "5'5", 110, "Japanese", "Actress")
name, age, height, weight, ethnicity, occupation = stats
print(name, age, height, weight, ethnicity, occupation)
"""

#output multiple data types (ik we did this already)
"""
age = 16
name = "Angel"
grade = 10
print(name,"is in grade",grade,"and is",age,"years old.")
"""

#Student smart or dumb comment, lmao
#name = "Duke"
#overallScore = -1092092190
"""
name = ("Duke", "Harry", "Charlise", "Riyo", "Hanra")
overallScore = (30, 50, 70, 90, 100)   
def grades(name, overallScore):
    if overallScore < 0 or overallScore > 100:
        print(name,"has an invalid score. Please try again.")
    elif 50 <= overallScore < 70:
        print(name,"is average.")
    elif 0<= overallScore <= 30:
        print(name,"is doomed.")
    elif overallScore < 50:
        print(name,"is developing.")
    elif overallScore >= 70:
        print(name,"has potential.")
    elif overallScore >= 90 < 100:
        print(name,"is very smart!")
    else:
        print(name,"has an invalid score. Please try again.")
for name, overallScore in zip(name, overallScore):
    grades(name[1], overallScore[1])
"""

"""
students = ("Duke", "Harry", "Charlise", "Riyo", "Hanra")
scores = (30, 50, 70, 90, 100)

def grades(name, overallScore):
    if overallScore < 0 or overallScore > 100:
        print(name, "has an invalid score. Please try again.")
    elif overallScore <= 30:
        print(name, "is doomed.")
    elif overallScore < 50:
        print(name, "is developing.")
    elif overallScore < 70:
        print(name, "is average.")
    elif overallScore >= 90:
        print(name, "is very smart!")
    else:
        print(name, "has potential.")


# Option A: run grades for everyone
for student, score in zip(students, scores):
    grades(student, score)

# Option B: check just one student (e.g. Harry, position 1)grades(students[1], scores[1])
"""
'''
x = 5
x = complex(x)
print(x)
'''

#x = "John Doe"
#print(x[1:5])

txt="my name is scar, and i am really energetic"
if "tired" not in txt:
        print("Scan Complete. Subject Scar = Tired Status NOT Detected.")