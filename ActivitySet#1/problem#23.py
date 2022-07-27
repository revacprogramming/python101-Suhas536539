import urllib.request, urllib.parse, urllib.error
import json
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
print('Retreving',url)
data = urllib.request.urlopen(url, context=ctx).read()
info = json.loads(data)

print('Retreved ',len(info["comments"]),'charecters')
sum=0
count=0
for item in info["comments"]:
    sum=sum+int(item['count'])
    count=count+1
print('sum:',sum)
print('count:',count