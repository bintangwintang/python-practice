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

#txt="my name is scar, and i am really energetic"
#if "tired" not in txt:
#        print("Scan Complete. Subject Scar = Tired Status NOT Detected.")

#playerhealth
'''
playerHealth = 1000
enemyAttack = 200
specialEnemyAttack = 500

playerHealth -= enemyAttack
playerHealth -= specialEnemyAttack
if playerHealth <= 0:
    print("You are dead.")
else:
    print(f"You have {playerHealth} health remaining.")
'''
'''
x = 5
if isinstance(x, int):
    print("x is an integer.")
else:
    print("x is not an integer.")
'''
'''
#left over money
month_Money = 4000
food = 500
bills = 1000
clothing = 300

total = month_Money - (food + bills + clothing)
print(f"You have {total} left over this month. Good job!") #i love you f-strings
'''

#x = 6
#y = 3

#print(x^y)
#6 = 0110
#3 = 0011
#^ = 0101


#dictionary test
#studentA = {
'''
    "name": "Rudy",
    "age": 17,
    "grade": 11,
    "strengths": "intelligent",
    "weaknesses": "lazy",
    "gradeRanking": "3 out of 178 students."
}

print(studentA["name"])
'''

#nested dict practice
#a = {'name' : 'John', 'age' : 20}
#b = {'name' : 'May', 'age' : 23}
#customers = {'c1' : a, 'c2' : b}
#for x, obj in customers.items():
#  print(x)
    
#  for y in obj:
#    print(y + ':', obj[y])

'''
breakdown of nested dict practice (line 148-156):

**customers = {'c1' : a, 'c2' : b}** is just a dictionary, like every other dictionary ive studied.
the values themselves are simply just other dictionaries.

so, the outer loop: **for x, obj in customers.items():** isn't doing anything fancier than i'm aware of!
its simply looping through the keys(x) and the values(obj) of customers (as we called customers.items()).
what this means, is that **x** is equal, to the key of customers, which would mean this;

x = 'c1' and 'c2' (as those two are the keys for customers)
&   
obj = a and b (as those two are the values for customers) -- which also just HAPPEN to be dictionaries themselves.


the inner loop isn't anything fancy either! you just need another loop to unpack 'a' and 'b' as those two are dictionaries, like customers!
so the inner loop is **for y in obj:** 
again, it's simply looping through the keys(y) in obj (which is the dictionaries themselves, a and b)
what this means is that **y** is equal to the keys of both dictionaries, a and b, meaning;

y = 'name' and 'age' (as those are the keys for both dictionaries)
&
obj[y] = the specific value for each key in both dictionaries, as obj IS either a or b, a coming first, b coming second (as we're incrementing with each loop)

soooo.... round 1 with obj[y]

y = 'name'
obj[y] = 'John'
&
y = 'age'
obj[y] = 20

round 2 with obj[y]

y = 'name'
obj[y] = 'May'
&
y = 'age'
obj[y] = 23


kapiche, me?

'''

#nested dict rep practice solo (rpg weapons inspiration)

#weapons rpg nested dict practice
'''
lightWep = {'name': 'Fang of Catastrophe', 'rarity': 'Legendary Tier', 'atk': 125, 'enchantedCheck': True}
mediumWep = {'name': 'Copper Shortsword', 'rarity': 'Common Tier', 'atk': 10, 'enchantedCheck': False}
heavyWep = {'name': 'Black-Iron Great Axe', 'rarity': 'Rare Tier', 'atk': 50, 'enchantedCheck': False}
wepInventory = {'Light': lightWep, 'Medium': mediumWep, 'Heavy': heavyWep}

for x, obj in wepInventory.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])
'''
"""
Light
name: Fang of Catastrophe
rarity: Legendary Tier

>you get the gist
>don’t spoil me, lemme find out if this shit is functional first, lol
"""
'''day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

#same as
day = 4
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")'''

'''month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")'''

#testing my understanding of match case w if statements
#rpg example again
'''
atk = 20
defence = 10
match atk:
  case _ if atk > defence:
    print("You win!")
  case _ if atk < defence:
    print("You lose!")
  case _ if atk == defence:
    print("Draw")
  case _:
    print("No match")
'''