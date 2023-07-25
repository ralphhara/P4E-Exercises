import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Ralph</name>
  <phone type="intl">+55 12 3456 7890</phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print(f"Phone: {tree.find('phone').text}")
print('Attr:', tree.find('email').get('hide'))