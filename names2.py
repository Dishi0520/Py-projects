# with open("names.txt", "r") as file:
    #for line in file:
        #print("hello,", line.rstrip())

names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}") 