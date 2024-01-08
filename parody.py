def main():
    x = int(input("What's X? "))
    if is_even(x):
        print(x, "is a even number")
    else:
        print(x, "is a odd number")

def is_even(n):
    if n%2 == 0:
        return True if n%2 == 0 else False


main()
