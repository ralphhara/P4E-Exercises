import json

data = '''
{
  "name" : "Ralph",
  "phone" : {
    "type" : "intl",
    "number" : "+55 12 3456 7890"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Phone:', info["phone"]["number"])
print('Hide:', info["email"]["hide"])
