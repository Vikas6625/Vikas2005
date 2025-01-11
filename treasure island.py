print("welcome to the treasure island! ")
print ("your aim is to find the the treasure")
choice1 = input('you\'re at a cross road,where do you wnt to go?'
                'type "left" or "right".: ').lower()
#there is a two way infront choose appropriate to find a way
if choice1 == "left":
    choice2 = input('you\'ve come to lake.'
                    'there is an island in the middle of the lake.'
                    'type "wait" to wait for a boat.'
                    'type "swim" to swim across.: ').lower()
    if choice2 == "wait":
        choice3 = input("you arrived at a island unharmed."
                        "there is a house with 3 doors. one red,"
                        "one yellow and onle blue."
                        "which colour do you choose? :").lower()
        if choice3 == "red":
            print("it's a room of fire.game over")
        elif choice2 == "yellow":
            print("you found the treasure. you won!")
        elif choice3 == "blue":
            print(" you enter a room of beasts.game over")
        else:
            print("you choose the door does not exists.game over")
    else:
        print("you got attacked by a angry trout.game over")

else:
    print("you fell in to a hole. game over")
