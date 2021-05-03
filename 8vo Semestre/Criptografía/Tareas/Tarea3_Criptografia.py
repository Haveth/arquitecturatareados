import math
from fractions import Fraction

print ('Calculadora de Entropía')
p1 = Fraction(input('Ingresa el primer argumento:  '))
p2 = Fraction(input('Ingresa el segundo argumento:  '))
log1 = math.log2(p1)
log2 =math.log2(p2)

entropia = ((p1)*log1)+((p2)*log2) 
entropia = entropia * (-1)

print ('La entropía es: ' + str(entropia))