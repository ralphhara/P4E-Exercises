import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Ralph</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Thais</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print(f'\nUser count: {len(lst)}\n')

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print(f"Attribute: {item.get('x')}\n")