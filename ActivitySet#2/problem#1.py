

def add(a, b):
    return  a+b


def main():
    a = int(input("enter the first number"))
    b = int(input("enter second number"))

    c = add(a, b)
    print ("Sum = ",c)


if __name__=='__main__':
    main()