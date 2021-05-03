import math


print ('Verifica congruencia dados tres números enteros a,b y modulo n')
a = int(input('Ingresa a:  '))
b = int(input('Ingresa b:  '))
n = int(input('Ingresa modulo :  '))


if a % n == b % n:
  print(str(a) + ' es congruente con ' + str(b) + ' módulo ' + str(n))
else:
  print(str(a) + ' no es congruente con ' + str(b) + ' módulo ' + str(n))
