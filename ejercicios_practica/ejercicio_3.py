# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese primero su nombre y luego su apellido
# Capture ambos datos e imprima su nombre completo
print('Ingrese por consola su nombre/s:')
nombre = str(input())

print('Ingrese por consola su apellido/s:')
apellido = str(input())

# Imprima su nombre completo

# Almacenar su nombre completo en una variable
# nombre_completo = .....

# Imprimir la cantidad de letras que posee su nombre completo
# cantidad_letras = len(....)


#Ejercicios Practica 3
#Autor: Bruno San Giorgio

nombre_completo= nombre +' '+ apellido  #Almacenamos el nombre completo en una variable

print('Su nombre es',nombre_completo)   #Imprimo el nombre completo

cantidad_letras= len(nombre_completo)   #Cuento la cantidad de letras nombre completo

cantidad_letras_real= cantidad_letras - 1   #Cuento la cantidad de letras reales sin el espacio

print('Su nombre completo tiene',cantidad_letras_real,'letras')    #Imprimo en consola la cantidad de letras del nombre completo