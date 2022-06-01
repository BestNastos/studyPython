import time

name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on dirt road, it has come to an end and you can turn left or right."
               " Where do you want to go? (type left / right) ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around or swim (type walk / swim) " )
    if answer == "swim":
        print("You swam across and were eaten by alligator")
    elif answer == "walk":
        print("You walked many miles, ran out of water and lost the game")
    else:
        print("Not a valid option, You lose")


elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back? (type cross/back) ")
    if answer == "back":
        print("You go back home. Because you are boring.")
        time.sleep(3)
        print("You lose.")
        time.sleep(1)
        print("YOU SUCK,", name.upper())
    elif answer == "cross":
        print("You cross the bridge and find a skeleton with treasure. The treasure is now yours. You win.")
    else:
        print("Not a valid option, You lose")
else:
    print("Not a valid option, You lose")