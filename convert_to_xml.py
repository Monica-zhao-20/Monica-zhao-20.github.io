# convert_to_xml.py
import json
import xml.etree.ElementTree as ET
from xml.dom import minidom

with open("restaurants.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# data is a dict; the list you want is under "restaurants"
items = data["restaurants"]

root = ET.Element("restaurants")

for r in items:
    r_elem = ET.SubElement(root, "restaurant")
    for key, value in r.items():
        child = ET.SubElement(r_elem, key)
        child.text = str(value)

# Pretty-print
rough = ET.tostring(root, encoding="utf-8")
parsed = minidom.parseString(rough)
pretty_xml = parsed.toprettyxml(indent="  ", encoding="utf-8")

with open("restaurants.xml", "wb") as f:
    f.write(pretty_xml)

print("✅ Conversion complete! File saved as restaurants.xml")