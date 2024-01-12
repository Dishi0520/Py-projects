def main():
    x = int(input("What's X? "))
    print("X squared is", square(x))

def square(n):
    return n * n

if __name__ == '__main__':
    main()