str= "X-DSPAM-Confidence: 0.8475"

pos = str.find(':')
print(pos)
line = str[pos + 2]
print(line)
value = float(line)
print(value)