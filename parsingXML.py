import xml.etree.ElementTree as ET

tree = ET.parse('lafayette.xml')


#Obtenir l'élément racine
root = tree.getroot()

#Affichage de l'élément racine
x = root.tag

print("valeur de x :" + x)



for child in root:
    print(child.tag, child.attrib)

