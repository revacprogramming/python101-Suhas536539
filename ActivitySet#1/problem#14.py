import xml.etree.Elementtree as ET
data = '''
<person>
<name>ABCD</name>
<phone type = " intl ">
</phone>
<email hide = "yes">
</person> '''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
