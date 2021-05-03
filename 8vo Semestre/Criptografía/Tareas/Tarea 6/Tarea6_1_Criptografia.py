import math


print ('Calculadora Algoritmo de Euclides (MCD de dos números)')
n1 = int(input('Ingresa el primer número:  '))
n2 = int(input('Ingresa el segundo número:  '))

residuo = 1
while residuo != 0:
  residuo = n1 % n2
  print ('MCD('+ str(n1) + ',' + str(n2) + ')',end="")
  if residuo != 0:
    n1 = n2
    n2 = residuo
    print(' = ',end="")
    
print(' = '+str(n2))
