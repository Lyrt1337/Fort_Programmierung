# Parameter

x=12.345678; y= -3.456789; ME= "cm"; prec=3;

# Ausgabe

print(x)
print(f"x= {x}")
print(f"x= {x} {ME}")

#Anzahl Dezimalstellen
print(f"x= {x:#.4} {ME}")
print(f"x= {x:#.{prec}} {ME}")
print(f"x= {x:#.{prec}} {ME} und y= {y:#.{prec}} {ME}")
