arcoiris=("azul", "verde", "rojo", "morado")
print(arcoiris)
print("-longitud arcoiris_")
print(len(arcoiris))
animales=("pantero", 20, "estatura", 69)
print(animales)
print("-elemantos de la tupla-")
print(animales[2])

rateros=("luis", "cesar", "edgar")
y=list(rateros)
y[0]="edgar"
x=tuple(y)
print(x)
print("agregando elementos")
Nanimal=("boby", "elmen")
y=list(Nanimal)
print(y)
y.append("bobin")
otratupla=tuple(y)

print(otratupla)
print("Uso de for en tuplas")
for elcolor in arcoiris:
  print(elcolor)