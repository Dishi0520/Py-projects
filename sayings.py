def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")


# __name__ means when you run a file from the command line

if __name__== '__main__':
    main()