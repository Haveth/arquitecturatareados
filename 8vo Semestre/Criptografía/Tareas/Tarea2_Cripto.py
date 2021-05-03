def formato(texto):
        texto=texto.replace(' ','')
        texto=texto.replace("j","i")

        if (len(texto)% 2 != 0):
            texto= texto+'x'
        
        return texto
    
def Cifrado(letra1,letra2,arreglo):
        L1x=0
        L1y=0
        
        for i in range(0,5):
            for j in range(0,5):
                if letra1 == arreglo[i][j]:
                    L1x=j
                    L1y=i
                    break
                 
        L2x=0
        L2y=0
        for i in range(0,5):
            for j in range(0,5):
                if letra2 == arreglo[i][j]:
                    L2x=j
                    L2y=i
                    break     

        if L1y==L2y:
            L1x+=1
            L2x+=1
               
        elif(L1x==L2x):
            L1y+=1
            L2y+=1
                  
        elif((L1x!=L2x) and (L1y!=L2y)):
            Lsaved=L1x
            L1x=L2x
            L2x= Lsaved                  
        L1x=desborde(L1x)
        L1y=desborde(L1y)
        L2x=desborde(L2x)
        L2y=desborde(L2y)
        
        return arreglo[L1y][L1x]+arreglo[L2y][L2x]

def desborde(num):
    if(num>4):
        return num-5
    return num

def decifrado(letra1,letra2,arreglo):
        L1x=0
        L1y=0
            
        for i in range(0, 5):
            for j in range(0, 5):
                if letra1==arreglo[i][j]:
                    L1x=j
                    L1y=i
                    break
        
        L2x=0
        L2y=0

        for i in range(0, 5):
            for j in range(0, 5):
                if letra2==arreglo[i][j]:
                    L2x=j
                    L2y=i
                    break

        
        if (L1y==L2y):
            L1x-=1
            L2x-=1
            
        
        elif L1x==L2x:
            L1y-=1
            L2y-=1
            
        
        elif((L1x!=L2x) and (L1y!=L2y)):
            Lsaved=L1x
            L1x=L2x
            L2x= Lsaved     
        
        L1x=desbordeinf(L1x)
        L1y=desbordeinf(L1y)
        L2x=desbordeinf(L2x)
        L2y=desbordeinf(L2y)
        return arreglo[L1y][L1x]+arreglo[L2y][L2x]

def desbordeinf(num):
    if(num<0):
        return num+5
    return num

class polybius():    
    def polCifrado(self,s):
        
        encpt=""
        
        for char in s:
            
            row = int((ord(char) - ord('a')) / 5) + 1
            
            col = ((ord(char) - ord('a')) % 5) + 1
            
            if char == 'k':
                row = row - 1
                col = 5 - col + 1
            
            elif ord(char) >= ord('j'):
                if col == 1 :
                    col = 6
                    row = row - 1
                col = col - 1

            r=str(row)
            c=str(col)
            encpt = encpt+r+c
        
        return encpt

    def polDescifrado(self,s):
        s1 = list(s)
        decpt = ""
        
        for i in range(0,len(s),2):
            r = int(s1[i])
            c = int(s1[i+1])
            ch = chr(((r-1)*5+c+96))
            if (ord(ch)-96>=10):
                ch = chr(((r-1)*5+c+96+1))
            ch1 = str(ch)
            decpt = decpt + ch1
        
        return decpt

class playfair():
    
    def playfairCifrar(self,texto):
        textoMin = texto.lower()

        arreglo = [['a', 'b', 'c', 'd', 'e'],['f', 'g', 'h', 'i', 'k'],['l', 'm', 'n', 'o', 'p'],['q', 'r', 's', 't', 'u'],['v', 'w', 'x', 'y', 'z']]

        textoMin=formato(textoMin)
        
        msCifrado=''
        for i in range(1,len(textoMin),2):
            msCifrado= msCifrado+Cifrado(textoMin[i-1],textoMin[i],arreglo)
            
            
        print(msCifrado)
        return msCifrado		


    def playfairDecifrar (self,texto):
        textoMin=texto.lower()
        arreglo=[['a','b','c','d','e'],['f','g','h','i','k'],['l','m','n','o','p'],['q','r','s','t','u'],['v','w','x','y','z']]
        
        textoMin = formato(textoMin)
        msCifrado = ''
        for i in range(1, len(textoMin),2):
            msCifrado = msCifrado+decifrado(textoMin[i-1],textoMin[i],arreglo)
            

        return msCifrado[0:len(msCifrado)]

class alberti():
    def albertiCif(self,mensaje, disco1, disco2):
        mensaje  = mensaje.lower()
        disco1  = disco1.lower()
        disco2  = disco2.lower()
        
        abc = 'abcdefghijklmnopqrstuvwxyz'
        rotDisc1=''
        rotDisc2=''
        idxDisco1 = abc.index(disco1)
        idxDisco2 = abc.index(disco2)

        x = len(abc)
        for i in range (idxDisco1,x):
            rotDisc1 = rotDisc1 + abc[i]
        
        if len(abc)!=len(rotDisc1):
            
            for i in range (0,idxDisco1):
                rotDisc1 = rotDisc1 + abc[i]
        
        for i in range (idxDisco2,x):
            rotDisc2 = rotDisc2 + abc[i]
        
        if len(abc)!=len(rotDisc2):
            
            for i in range (0,idxDisco2):
                rotDisc2 = rotDisc2 + abc[i]
      
        mensajeCifrado = ''
        for x in mensaje:
            if x!=' ':
                mensajeCifrado = mensajeCifrado + rotDisc2[rotDisc1.index(x)]
            else:
                mensajeCifrado = mensajeCifrado +' '
        return mensajeCifrado

    def albertiDes(self,mensaje, disco1, disco2):
        mensaje  = mensaje.lower()
        disco1  = disco1.lower()
        disco2  = disco2.lower()
        
        abc = 'abcdefghijklmnopqrstuvwxyz'
        rotDisc1=''
        rotDisc2=''
        idxDisco1 = abc.index(disco1)
        idxDisco2 = abc.index(disco2)

        x = len(abc)
        for i in range (idxDisco1,x):
            rotDisc1 = rotDisc1 + abc[i]
        
        if len(abc)!=len(rotDisc1):
            
            for i in range (0,idxDisco1):
                rotDisc1 = rotDisc1 + abc[i]
        
        for i in range (idxDisco2,x):
            rotDisc2 = rotDisc2 + abc[i]
        
        if len(abc)!=len(rotDisc2):
            
            for i in range (0,idxDisco2):
                rotDisc2 = rotDisc2 + abc[i]

        mensajeCifrado = ''
        for x in mensaje:
            if x!=' ':
                mensajeCifrado = mensajeCifrado + rotDisc1[rotDisc2.index(x)]
            else:
                mensajeCifrado = mensajeCifrado +' '
        return mensajeCifrado

class vigenere():
    def vigenereCifrado(self,texto):
        abecedario = "abcdefghijklmnopqrstuvwxyz"
        input_string = ""
        enc_key = ""
        enc_string = ""

        enc_key = input("Introduce una llave de cifrado: ")
        enc_key = enc_key.lower()

        input_string = input("Introduce el texto: ")
        input_string = input_string.lower()

        string_length = len(input_string)

        llave_expandida = enc_key
        longitud_llave = len(llave_expandida)

        while longitud_llave < string_length:

            llave_expandida = llave_expandida + enc_key
            longitud_llave = len(llave_expandida)

        key_position = 0

        for letra in input_string:
            if letra in abecedario:
                position = abecedario.find(letra)
                key_character = llave_expandida[key_position]
                key_character_position = abecedario.find(key_character)
                key_position = key_position + 1
                new_position = position + key_character_position
                if new_position > 26:
                    new_position = new_position - 26
                new_character = abecedario[new_position]
                enc_string = enc_string + new_character
            else:
                enc_string = enc_string + letra
        return(enc_string)


    def vigenereDescifrado(self,texto):
        abecedario = "abcdefghijklmnopqrstuvwxyz"
        input_string = ""
        dec_key = ""
        dec_string = ""

        dec_key = input("Introduce una llave de cifrado: ")
        dec_key = dec_key.lower()

        input_string = input("Introduce el texto: ")
        input_string = input_string.lower()

        string_length = len(input_string)

        llave_expandida = dec_key
        longitud_llave = len(llave_expandida)

        while longitud_llave < string_length:

            llave_expandida = llave_expandida + dec_key
            longitud_llave = len(llave_expandida)

        key_position = 0

        for letra in input_string:
            if letra in abecedario:

                position = abecedario.find(letra)

                key_character = llave_expandida[key_position]
                key_character_position = abecedario.find(key_character)
                key_position = key_position + 1

                new_position = position - key_character_position
                if new_position > 26:
                    new_position = new_position + 26
                new_character = abecedario[new_position]
                dec_string = dec_string + new_character
            else:
                dec_string = dec_string + letra
        return(dec_string)
    
class cesar():
    def cesarCifrado(self,texto):
        abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuwxyz" 
        k = 23
        cifrado=""
        texto  = texto.lower()
        for c in texto:
            if c in abc:
                cifrado += abc[(abc.index(c)+k)%(len(abc))]
            else:
                cifrado+=c
        
        cifrado  = cifrado.lower()
        return cifrado
    
    def cesDescifrado(self,texto):
        texto  = texto.lower()
        abc = 'abcdefghijklmnñopqrstuvwxyz'
        llave = 'xyzabcdefghijklmnñopqrstuvw'
        decpt = ''
        for x in texto:
            if x!=' ':
                decpt = decpt + abc[llave.index(x)]
        else:
            decpt = decpt +' '
        return decpt

class menu():

    def seleccion(self, opcion):
        pol = polybius()
        ces = cesar()
        vig = vigenere()
        alber = alberti()
        playf = playfair()
        
        palabra = input('Escribe la palabra que deseas Cifrar:   ')
        if opcion == '1':
            texto = pol.polCifrado(palabra)
            print("Texto cifrado: ", texto)
            texto2 = input('Texto a descifrar: ')
            decpt = pol.polDescifrado(texto2)
            print("Texto descifrado: ",decpt)   
        if opcion == '2':
            texto = ces.cesarCifrado(palabra)
            print("Texto cifrado: ", texto)
            texto2 = input('Texto a descifrar: ')
            decpt = ces.cesDescifrado(texto2)
            print("Texto descifrado: ",decpt) 
        if opcion == '3':
            print('Dame el mensaje a cifrar: ')
            msj = input()
            d1 = input('Letra del disco uno: ')
            d2 = input('Letra del disco dos: ')
            print('El resultado es: '+ alber.albertiCif(msj,d1,d2))  
            print(' ')
            print('Dame el mensaje a descifrar: ')
            msj = input()
            d3 = input('Letra del disco uno: ')
            d4 = input('Letra del disco dos: ')
            print('El resultado es: '+ alber.albertiDes(msj,d3,d4))  
            
        if opcion == '4':
            print(' ')
            texto = vig.vigenereCifrado(palabra)
            print("Texto cifrado: ", texto)
            print(' ')
            decpt = vig.vigenereDescifrado(texto)
            print("Texto descifrado: ",decpt)
        if opcion == '5':
            print('Playfair cifrado : '+ playf.playfairCifrar(palabra))
            descifrar = input('Dame el mensaje a descifrar: ')
            print('El resultado es: '+ playf.playfairDecifrar(descifrar))
        return 1


if __name__ == "__main__":
    print('1.- Cifrado/Descifrado Polybios')
    print('2.- Cifrado/Descifrado Cesar')
    print('3.- Cifrado/Descifrado Alberti')
    print('4.- Cifrado/Descifrado Vigénere')
    print('5.- Cifrado/Descifrado Playfair')
    print(' ')
    opcion = input('Selecciona la operación deseada:  ')
    menu = menu()
    menu.seleccion(opcion)



