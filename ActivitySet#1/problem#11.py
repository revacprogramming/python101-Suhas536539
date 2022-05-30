fname = input('enter file: ')
if len(fname) < : fname = 'clown.txt'
hand = open(fname)
 
 di = dict()
 for lin in hand:
     lin = lin.strip()
     wds = lin.split()
     for w in wds:
         di[w] = di.get(w,0) + 1

print(di)
x = sorted(di.items())
print(x)