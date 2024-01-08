user_name=input("What is your name: ").strip().title()
#  Remove whitespace from str and capitalize users name

# Split User Name into first naem and last name
first, last = user_name.split(" ")
print(f"Hello, {first}")

print("Hello, " + first)
