from lxml import etree
root = etree.parse("data/lshw.xml")

# print xml
print(etree.tostring(root, pretty_print=True, encoding=str))

# -------------------------------------------------------------------------
# GUTE LINKS DAZU (Generatoren)
# http://xpather.com/

# XML auf diese Seite reinkopieren
# Dann halten STRG-Taste gedrückt und mit Mauszeiger darüber.

# zum prüfen: Bsp. //node[@id='memory']/size    ins schwarze Feld kopieren

# -------------------------------------------------------------------------

print('')
print('-------------------------------------------------------------------------------------------')

print('Aufgabe 2: XML und XPath (lshw.xml) / FHGR Juni 2023, Gilomen Christian')

print('-------------------------------------------------------------------------------------------')

# ------
# Memory
# ------
print('memory size node:              ', root.xpath("//node[@id='memory']/size"))
print('memory size text:              ', root.xpath("//node[@id='memory']/size/text()"))
print('memory[1] size[1]:             ', root.xpath("//node[@id='memory'][1]/size[1]/text()"))

print('-------------------------------------------------------------------------------------------')

# ---
# CPU
# ---
print('cpu product node:              ', root.xpath("//node[@id='cpu']/product"))
print('cpu product text:              ', root.xpath("//node[@id='cpu']/product/text()"))
print('cpu[1] product[1] text:        ', root.xpath("//node[@id='cpu'][1]/product[1]/text()"))

print('-------------------------------------------------------------------------------------------')

# ------------
# IDE IO-Ports
# ------------
print('ide node:                      ', root.xpath("//node[@id='ide'][1]/resources[1]/resource[2]"))
print('ide ioport type:               ', root.xpath("//node[@id='ide'][1]/resources[1]/resource[2]/@type"))
print('ide ioport value:              ', root.xpath("//node[@id='ide'][1]/resources[1]/resource[2]/@value"))

# ergibt eine Liste aller resource-Einträge (IDE)
print('ide resource value:            ', root.xpath("//node[@id='ide'][1]/resources[1]/resource/@value"))

# nur type 'ioport'
print('ide resource ioport value:     ', root.xpath("//node[@id='ide']/resources/resource[@type = 'ioport']/@value"))

# Count ermitteln => ev. für eine Schlaufe zu verwenden...
print('ide resource ioport count:     ', root.xpath("count(//node[@id='ide']/resources/resource[@type = 'ioport'])"))

print('')

# Problem hier ist der Index, weil nicht forlaufend !!!!!!!!!!!!!! => show ioport
y = root.xpath("count(//node[@id='ide']/resources/resource[@type = 'ioport'])")
x = 0

for x in range(x, 8):
    # print('ide resource ioport count:     ', root.xpath("//node[@id='ide']/resources/resource[x][@type = 'ioport']/@value"))
    print('ide resource ioport count:     ', root.xpath("//node[@id='ide']/resources/resource[" + str(x) +"][@type = 'ioport']/@value"))
    # print(x)
print('')
print('X ide resource ioport count:     ', root.xpath("//node[@id='ide']/resources[1]/resource[0][@type = 'ioport']/@value"))
print('X ide resource ioport count:     ', root.xpath("//node[@id='ide']/resources[1]/resource[1][@type = 'ioport']/@value"))
print('X ide resource ioport count:     ', root.xpath("//node[@id='ide']/resources[1]/resource[2][@type = 'ioport']/@value"))
print('X ide resource ioport count:     ', root.xpath("//node[@id='ide']/resources[1]/resource[3][@type = 'ioport']/@value"))
print('X ide resource ioport count:     ', root.xpath("//node[@id='ide']/resources[1]/resource[4][@type = 'ioport']/@value"))
print('X ide resource ioport count:     ', root.xpath("//node[@id='ide']/resources[1]/resource[5][@type = 'ioport']/@value"))
print('X ide resource ioport count:     ', root.xpath("//node[@id='ide']/resources[1]/resource[6][@type = 'ioport']/@value"))
print('X ide resource ioport count:     ', root.xpath("//node[@id='ide']/resources[1]/resource[7][@type = 'ioport']/@value"))
print('-------------------------------------------------------------------------------------------')

# -----------------
# Audio CD playback
# -----------------
print('Audio CD playback node:        ', root.xpath("//capability[@id='audio']"))
print('Audio CD playback node:        ', root.xpath("//capability[@id='audio']/text()"))
print('Gerät direct:                  ', root.xpath("//node[@id='cdrom']/description/text()"))

# Eltern-node
print('Parent node:                   ', root.xpath("//capability[@id='audio']/parent::node()/parent::node()"))
# direkt via "Audio CD playback"... über 2 Elternnodes die description ausgeben
print('Audio CD playback node:        ', root.xpath("//capability[@id='audio']/parent::node()/parent::node()/description/text()"))

print('-------------------------------------------------------------------------------------------')

# -----------------------
# handle(s) via Icon disc
# -----------------------
# alle mit icon + disc
print('Icon disc:                     ', root.xpath("//hints/hint[@name='icon' and @value='disc']"))
# Eltern-node
print('Icon disc parent node:         ', root.xpath("//hints/hint[@name='icon' and @value='disc']/parent::node()/parent::node()"))
# direkt via "Icon disc"... über 2 Elternnodes die handle ausgeben
print('Icon disc / handle:            ', root.xpath("//hints/hint[@name='icon' and @value='disc']/parent::node()/parent::node()/@handle"))

print('')

print('-------------------------------------------------------------------------------------------')
print('Zur Lösung der Aufgabe, reichen folgende Anweisungen (Rest oben ist für reines Verständnis:')
print('(5 Anweisungen)')
print('-------------------------------------------------------------------------------------------')

print('1. memory size text:           ', root.xpath("//node[@id='memory']/size/text()"))
print('2. cpu product text:           ', root.xpath("//node[@id='cpu']/product/text()"))
print('3. ide resource ioport value:  ', root.xpath("//node[@id='ide']/resources/resource[@type = 'ioport']/@value"))
print('4. Audio CD playback => Gerät: ', root.xpath("//capability[@id='audio']/parent::node()/parent::node()/description/text()"))
print('5. Icon disc / handle:         ', root.xpath("//hints/hint[@name='icon' and @value='disc']/parent::node()/parent::node()/@handle"))
print('-------------------------------------------------------------------------------------------')

print('')
print('Grüassli Papa ;-)')
