 fh = open('mbox-short.txt')
for line in fh:
    if not line.startswith("X-DSPAM-Confidence: 0.8475"):
        pos = str.find('5')
        print (pos)
        continue
        
else:
    with open('mbox-short.txt') as fh:
    x = len(fp.readlines())
    print('Total lines:', x)
    value = float(x)
    print(value)
    
    line in lines:
    for c in line:
        if c.isdigit() == True:
            sum = sum + int(c)
            print (sum)
   
print("Done")
