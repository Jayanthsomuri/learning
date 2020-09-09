
import random
print("welcome to the dice stimulator")
r1=random.randint(1,6)
while True:
    print("you rolled the dice",r1)
    r1=random.randint(1,6)
    print("choice Y=yes\n N=no")
    user_input=(input("enter Yes or N:"))
    if user_input=="N":
        break
    else:
        continue
