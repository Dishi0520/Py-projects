name = input("Type your name: ")
print("Welcome", name, "to this awesome adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":

        answertwo = input("You come to a river, you can walk around it or swim across. Type walk to walk around it or swim to swim across. ").lower()

        if answertwo == "swim":
            print("You swam across and got eaten by an an alligator")
        elif answertwo == "walk":
            print("You walked along the banks of the river, avoiding the alligators, and crossed safely. Congrats! You passed.")
            answertwo_1 = input("You come across a bear. Do you feed it your food or do you walk away slowly. Say feed to feed and walk to walk. ").lower()

            if answertwo_1 == "feed":
                   print("You gave the bear all your food and he wanted more, so he ate you. Try again.")
                   quit()
            elif answertwo_1 == "walk":
                   print("You slowly walk away and escape the bear. Congrats! You're almost home.")

            else:
                print("Not a valid option. Try again!")
            answertwo_2 = input("Finally, you can see the city! What should you do? Wait for daylight or go in the night? Type daylight for waiting and night for going right now. ").lower()
            if answertwo_2 == "daylight":
                print("Yay! You found shelter and hitched a ride back to the city, safe and sound. You finished! Congrats.")

            elif answertwo_2 == "night":
                print("You walked in the dark and came across a coyote who surprise attacked you! You lose. try again.")
                quit()
        else:
            print("Not a valid option. Try again.")
elif answer == "right":
    answerthree = input("You came upon a bridge. It looks wobbly. Do you want to cross it, or go back? Type cross to cross it and back to go back. ").lower()

    if answerthree == "back":
        print("You start going back, but end up getting lost. you meet a hungry bear and die. You lost. Try again.")
    elif answerthree == "cross":
        print("You start crossing the river and accidently step on a loose board and fall into the river below. You can't swim and you die. Try again.")
    else:
        print("Not a valid option. You lost.")


else:
    print("Not a valid option. You lose. Pick left of right next time.")

print("Thank you for playing,", name,)