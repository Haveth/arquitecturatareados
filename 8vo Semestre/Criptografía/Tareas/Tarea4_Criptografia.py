import math


print ('Calculadora de distancia de Hamming a nivel de bit')
p1 = input('Ingresa la primer cadena:  ')
p2 = input('Ingresa la segunda cadena:  ')

p1_convertido = p1
p2_convertido = p2

a_byte_array = bytearray(p1_convertido, "utf8")
a_byte_array2 = bytearray(p2_convertido, "utf8")

byte_list = []
byte_list2 = []

for byte in a_byte_array:
    binary_representation = bin(byte)
    byte_list.append(binary_representation)
    
for byte in a_byte_array2:
    binary_representation2 = bin(byte)
    byte_list2.append(binary_representation2)
    
print(byte_list)
print(byte_list2)

def distancia(b1, b2): 
    cont_distancia = 0 
    for n in range(len(byte_list)): 
        if byte_list[n] != byte_list2[n]: 
            cont_distancia += 1 
    print ('La distancia de Hamming es : ' + str(cont_distancia))
    return cont_distancia 

distancia(byte_list,byte_list2)

