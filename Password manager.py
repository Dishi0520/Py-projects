from cryptography.fernet import Fernet


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)
access = str("Dishi<3M@rvel!")

masterpwd = input("What is the master password? ")
if masterpwd != access:
    quit()
key = load_key() + masterpwd.encode()
fer = Fernet(key)

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) '''


def view():
    with open("passwords2.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            website, user, pwd2 = data.split("|")
            print("Website:", website, "| Username:", user, "| Password:", fer.decrypt(pwd2.encode()).decode())


def add():
    account = input("Name of the website: ")
    name = input("Username: ")
    pwd = input("Password: ")

    with open("passwords2.txt", 'a') as f:
        f.write(account + "|" + name + "|" + fer.encrypt(pwd.encode()).decode() + "|" + "\n")
        print("Password has been added!")


while True:
    mode = input("Would you like to add a new password or view existing ones (view/add) press q to quit. ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue