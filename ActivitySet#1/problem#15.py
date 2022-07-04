import json
data = '''
{
"name" = "ABCD",
"phone" = {
    "type"="intl"
    "number" = "1234567890"
    },
 "email":{
"hide"="yes"
 }
}'''

info = json.loads(data)
print('Name:',info["name"])
print('Hide:',info["email"]["hide"]) 