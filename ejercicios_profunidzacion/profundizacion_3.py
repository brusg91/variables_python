# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con cadenas
'''
Enunciado:
Realice un programa que reciba por consola su nombre completo
e imprima en pantalla su nombre en los siguientes formatos:
- Todas las letras en minúsculas
- Todas las letras en mayúsculas
- Solo la primera letra del nombre en mayúscula

NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
de strings:
- lower
- upper
- capitalize

Puede buscar en internet como usar en Python estos métodos.
Les dejamos el siguiente link que posee casos de uso de algunos de ellos:

Link de referencia:
https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

Cualquier duda con estos métodos pueden consultarla por el campus
'''

import string


print('Ahora si! buena suerte')
# Empezar aquí la resolución del ejercicio


#Ejercicios Prfundizacion 3
#Autor: Bruno San Giorgio

print('Ingrese su nombre completo') #Pido por consola el nombre 
nombre= str(input())

nombre_minus= nombre.lower()        #Variable todo minuscula
nombre_mayus= nombre.upper()        #Variable todo mayuscula
nombre_primera_mayuscula= nombre.capitalize()        #Variable primer letra mayuscula

print(nombre_minus)         #Imprimo por consola todo minuscula

print(nombre_mayus)         #Imprimo por consola todo mayuscula

print(nombre_primera_mayuscula)     #Imprimo por consola la primera en mayuscula
