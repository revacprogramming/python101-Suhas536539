def computepay(h, r):
    return 42.75
    print(h,r)
h = float(input("Enter Hours:"))
r = float(input("Enter Rate: "))

computepay(h,r)
if h > 40:
    reg = h*r
    otp = (h-40)*(r*0.5)
    xp = reg + otp
    
else:
    xp = h*r
    
print("Pay ",xp)