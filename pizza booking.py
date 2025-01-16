print("welcome for python pizza deliveries!")
size = input("what is the size of the pizza? S,M or L: ")
pepparoni = input("do you want pepparoni on the pizza? Y or N: ")
extra_cheese =input("do you need extra cheese? Y or N: ")

#size choice
bill = 0
if size=="S":
    bill +=15
elif size=="M":
    bill +=20
elif size=="L":
    bill +=25
else:
    print("you have entered the wrong details")

#pepparoni choice
if pepparoni=="Y":
    bill +=2
else:
    bill +=3
#extra cheese
if extra_cheese=="Y":
    bill +=1

print(f"the final bill_amount={bill}")