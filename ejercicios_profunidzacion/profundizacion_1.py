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

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

from __future__ import division


print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio


#Ejercicios Prfundizacion 1
#Autor: Bruno San Giorgio

print('Ingresa un numero')
Numero_1= float(input())    #Solicito primer numero por consola
print('Ingresa otro numero')
Numero_2= float(input())    #Solicito otro numero por consola

Suma= Numero_1 + Numero_2   #Calculo la suma
print('La suma entre',Numero_1,'y',Numero_2,'es',Suma)  #Imprimo el calculo por consola

Resta= Numero_1 - Numero_2  #Calculo la resta
print('La resta entre',Numero_1,'y',Numero_2,'es',Resta)  #Imprimo el calculo por consola

Multiplicacion= Numero_1 * Numero_2   #Calculo la multiplicacion
print('La multiplicacion entre',Numero_1,'y',Numero_2,'es',Multiplicacion)  #Imprimo el calculo por consola

Division= Numero_1 / Numero_2   #Calculo la division
print('La division entre',Numero_1,'y',Numero_2,'es',Division)    #Imprimo el calculo por consola

Potencia= Numero_1 ** Numero_2    #Calculo la potencia
print('La potencia entre',Numero_1,'y',Numero_2,'es',Potencia)    #Imprimo el calculo por consola
