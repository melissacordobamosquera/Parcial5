'''
Este código muestra la probabilidad de que n sea un número perfecto
tomando n al azar
'''

import random

'Funcion para saber si n es primo, si es así, nos devuelve un 1, sino un 0'

def es_primo(n):       

    if n == 2:
        return 1    
    elif n == 3:
        return 1  
            
    elif n == 5:
        return 1  
            
    elif n == 7:
        return 1  
            
    elif (n % 2)!= 0 and (n % 3)!= 0 and (n % 5)!= 0 and (n % 7)!= 0 and n!=1:
        return 1 
    else: 
        return 0         

'Función para saber la cantidad de numeros perfectos que hay de 1 hasta n'

def cant_perfectos(n):

    contador = 0

    for i in range (n):

        if es_primo(i) == 1:   #Necesitamos que i sea primo para aplicar la formula

            formula = (2**(i-1))*((2**i) - 1)     #Formula para numeros perfectos

            if formula <= n:

                contador = contador + 1

            else:

                breakpoint           #Se detiene cuando el siguiente numero perfecto sea mayor que n

    return contador

'Realizamos n experimentos con a aleatorio'

def simulacion(n):

    contador = 0

    for i in range(n):

        a = random.randint(1,100)

        contador = contador + cant_perfectos(a)

    return contador/n            #esta es la probabilidad que buscamos


'''
Con esta prueba, podemos observar que a medida que n se hace grande, 
la probabilidad de que n sea un número perfecto disminuye"

'''

simulacion(10)
simulacion(100)
simulacion(1000)
simulacion(10000)
simulacion(100000)
