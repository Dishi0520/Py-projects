print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")


if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")
score = 0
answer = input("What does JCW stand for? ")
if answer.lower() == "ji chang wook":
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")

answer = input("Who dies in Mr. Sunshine? ")
if answer.lower() == "eugene choi":
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")

answer = input("Which K-pop group broke up recently? ")
if answer.upper() == "BTS":
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")

answer = input("Is BTS ever going to come back? ")
if answer.lower() == "no":
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%!.")

