import random
options = ["heads", "tails",]

user_input = input("Heads or Tails? Type Q to quit: ").lower()
random_number = random.randint(0, 1)
# Heads 0, Tails 1
computer_pick = options[random_number]
print("Computer picked", computer_pick + ".")

if user_input == computer_pick:
    print("You won!")
else: 
    print("You lost!")