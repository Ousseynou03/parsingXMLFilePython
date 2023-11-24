import xml.etree.ElementTree as ET

tree = ET.parse('lafayette.xml')

root = tree.getroot()

for url in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
    loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
    print(loc.text)