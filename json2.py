import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Ralph"
  } ,
  { "id" : "002",
    "x" : "7",
    "name" : "Thais"
  }
]'''

info = json.loads(data)
print(f'\nUser count: {len(info)}\n')

for item in info:
    print('Name:', item['name'])
    print('Id:', item['id'])
    print(f"Attribute: {item['x']}\n")