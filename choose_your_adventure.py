name = input("type your name:")
print("welcome", name, "to this adventure!")

answer = input(
    "you are on a dirt road , it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer =input(
        "you come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim accross:")
    
    if answer == "swim":
        print("you swam accorss and were eaten by an alligator.")
    elif answer == "walk":
        print("you walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. you lose.')


elif answer == "right":
    answer = input("you come to a bridge, it looks wobbly, do you want to cross it or hea back (cross/back)?")
    
    if answer == "back":
        print("you go back and lose.")
    elif answer == "cross":
        answer = input(
            "you cross the bridge and meet a stranges. Do you talk to then(yes/n0)?")
        
        if answer == "yes":
            print("you talk to the stranges and the give you gold. YOU WIN!")

        elif answer == "no":
            print("you ignore the stranger and they are offended snd you lose.")
        else:
            print("Not a valid option.you lose")
    else:
        print('not a valid option. You lose.')
else:
    print("Not a valid option.You lose.")

print("Thankyou for trying",name)