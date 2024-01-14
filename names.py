name = input("What's your name? ")
#open files/create file calles names.txt and write
# with: open file AS "file"
with open("names.txt", "a") as file:
#Writes input into file
    file.write(f"{name}\n")
#Saves and closes the file
#file.close
    


