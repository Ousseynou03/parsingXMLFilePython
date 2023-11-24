import xml.etree.ElementTree as ET

tree = ET.parse('nameEspace.xml')

root = tree.getroot()

#root = ET.fromstring('nameEspace.xml')

for actor in root.findall('{http://people.example.com}actor'):
    name = actor.find('{http://people.example.com}name')
    print(name.text)



