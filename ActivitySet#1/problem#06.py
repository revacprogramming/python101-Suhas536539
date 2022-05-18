largest = 0
smallest = 0
while True:
    n = float(input("Enter a number: "))
    if n == "done":
        break
    print(n)
    try:
        n = float(n)
    except:
            print('invalid input')
            continue
largest = max(n)
smallest = min(n)
print("Maximum :",largest)
print("Minimum :",smallest)
