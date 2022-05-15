h=float(input("enter the number of hrs"))
gp=10.50
if h<40:
    pay = h*gp
    print(' ',pay)
    
elif h>40:
    extra = h - 40
    gp2 = h*1.5
    pay1 = h*gp2
    print(' ',pay1)