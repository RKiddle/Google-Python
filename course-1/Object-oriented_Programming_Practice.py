#1 

blue.jay.count()
print(bluejay.number)

#2

# “If you have an apple and I have an apple and we exchange these apples, then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
  #"you" and "me" will exchange ALL our apples with one another

  you.apples = 2

  me.apples = 1
  return you.apples, me.apples
    
def exchange_ideas(you, me):
  #"you" and "me" will share our ideas with one another
  you.ideas = 2
  me.ideas = 2
  return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))
