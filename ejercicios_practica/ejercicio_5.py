# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese dos palabras y arme combinaciones con ella
print('Ingrese palabra 1:')
palabra_1 = str(input())

print('Ingrese palabra 2:')
palabra_2 = str(input())

# De la primera palabra tome las primeras tres letras, utilice el operador :
# De la segunda palabra tome las primeras dos letras, utilice el operador :
# Formar una nueva palabra con los recortes solicitados
# Imprima en pantalla los resultados


#Ejercicios Practica 4
#Autor: Bruno San Giorgio

primeras_tres_palabra_1= palabra_1[0:3] #Usamos el operador para tomar las primeras tres letras

primeras_dos_palabra_2= palabra_2[0:2]  #Usamos el operador para tomar las segundas dos letras

nueva_palabra=primeras_tres_palabra_1+primeras_dos_palabra_2    #Formamos una nueva palabra con los recortes

print(nueva_palabra)    #Imprimimos esta nueva palabra en la consola