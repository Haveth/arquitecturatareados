import math

print ('Dame la cadena para generar su HASH')
p1 = input('Ingresa el texto: ')

p1 = p1.ljust(16, '*')

p1_convertido = p1

a_byte_array = bytearray(p1_convertido, "utf8")

byte_list = []

for byte in a_byte_array:
    binary_representation = bin(byte)
    byte_list.append(binary_representation)
    
print(byte_list)

print (p1)




