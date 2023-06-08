from lxml import etree
root = etree.parse("data/cds104.xml")

# Auswahl von Knoten 1

# print(root.xpath("lecturer"))
# print(root.xpath("lecturer/*"))
# print(root.xpath("//name"))
# print(root.xpath("//name/.."))
# print(root.xpath("lecturer[1]"))

# Auswahl von Knoten 2

# print(root.xpath("*[@type]"))
# print(root.xpath("*[@type='internal']"))
# print(root.xpath("lecturer[name]"))
# print(root.xpath("lecturer[units='24']"))
# print(root.xpath("//*[.='24']"))

# Auswertung

# print(root.xpath("lecturer/@type"))
# print(root.xpath("//name/text()"))
# print(root.xpath("string(lecturer[1])"))
print(root.xpath("number(lecturer[1]/units)"))
