myStr = "Hello World"

#print(dir(myStr))
#.upper MAYUSCULAS
#.lower minusculas
# .swapcase cambiar mayus por minus viceversa
#.capitaliza primera letra en mayuscula
#.replace cambiar 
print(myStr.lower())
print(myStr.swapcase()) 
print(myStr.capitalize()) 
print(myStr.replace('Hello', 'fuck'))
print(myStr.replace('Hello', 'fuck').upper())
print(myStr.count('l'))

print(myStr.startswith('He'))

print(myStr.split())
#.split separa las "palabras" y las convierte en litas

print(myStr.find('p'))
#enuentra la posicion de la letra o palabra, incia desde cero, uno, dos....

print(len(myStr))
print(myStr.index('e'))

print(myStr.isnumeric())
#Para saber si es un valor numerico
print(myStr.isalpha())
