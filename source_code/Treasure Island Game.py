print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
user_choice_1 = input('You can turn left or right. Which direction do you choose?\n')

if user_choice_1 == "right":
    print("You fall in a hole and die. Game over.")
elif user_choice_1 == "left":

    user_choice_2 = input('You see a lake in the distance and you approach. Do you swim or wait?\n')
    if user_choice_2 == "swim":
        print('You are attacked by a giant Trout and die. Game over')
    elif user_choice_2 == "wait":
        print("While you're waiting you observe the area and notice a cabin. You enter and inside you see three doors. They are colored red, yellow, and blue.").lower()

        user_choice3 = input("Which do you take?\n")
        if user_choice3 == "red":
            print("You are teleported into a burning building. There is no escape and you are burned alive. Game over.")
        elif user_choice3 == "blue":
            print('You are teleported to a forest filled with beasts. You are eaten by the beasts. Game over.')
        elif user_choice3 == "yellow":
            print('You are teleported to a treasure room. Congratulations, you win!')
        else:
            print('That is not a valid option. Game over.')