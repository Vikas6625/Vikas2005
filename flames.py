print("check the relationship status between you and your crush right now:")
user = input("type 'play' to play FLAMES, 'end' to exit :")
is_on = True
while is_on:
    if user == "play":
        boy = input("enter your name:")
        girl = input("enter your crush's name:")
        dict = {}
        for i in boy:
            if i not in dict:
                dict[i] = 1
            elif i in dict:
                if dict[i] == 1:
                    dict[i] -= 1
                else:
                    dict[i] += 1
        for j in girl:
            if j not in dict:
                dict[j] = 1
            elif j in dict:
                if dict[j] ==1:
                    dict[j] -=1
                else:
                    dict[j] += 1
        num = 0
        for letter in dict:
            if dict[letter] == 1:
                num += 1
        res = ["Its F..you are born to be friends","Its L..you are made for each other","Its A..affection is holding between you together","Its M..time to think of the marriage","Its E..you both sre enemies"]
        while len(res) > 1:
            split_index = (num % len(res)-1)
            if split_index >= 0:
                right = res[split_index +1:]
                left = res[:split_index]
                res = right + left
            else:
                res = res[: len(res)-1]
        print(res[0])
        is_on = False
    elif user == "end":
        print("Thank you..hope you had a good time of playing with this game")
        is_on = False
    else:
        print("Invalid input!!")
        is_on = False