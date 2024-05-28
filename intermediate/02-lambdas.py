# Lambdas
""" 
Las Lambdas en Python son funciones anonimas que se definen en una sola linea
usando la palabra clave 'lambda'.

A diferencia de las funciones normales definidas con 'def', las lambdas no tienen nombre y generalmente
se utilizan para tareas simples y rapidas.

Las lambdas se pueden almacenar en una variable

La sintaxis basica es:
  lambda argumentos: expresión

Las Lambdas se utilizan comunmente en situaciones donde se requiere una funcion corta, como en funciones
de orden superior ('map', 'filter', 'reduce') o en situaciones donde una funcion rapida es 
suficiente y definir una funcion completa seria demasiado verbose.
"""

# Vamos a crear una funcion lambda para sumar dos valores
sum_two_values = lambda first_value, second_value: first_value + second_value
# Hacemos un print de la variable que se comporta como una funcion, a la cual podemos
# pasar valores entre parentesis.
print(sum_two_values(5, 6))

multiply_values = lambda value1, value2: value1 * value2
print(multiply_values(4,5))

# Lambda dentro de funciones
def sum_three_values(value3):
  return lambda value1, value2: value1 + value2 + value3

""" 
Primero llamamos a sum_three_values(3), que necesita de un parametro (3), lo que devuelve una 
lambda que espera dos arg en mi caso (1,2)
Inmediatamente despues, se llama a esa lambda con los valores (1,2) 
"""
my_sum = sum_three_values(3)(1,2)
print(my_sum)

# Se podria almacenar la lambda y llamarla mas tarde, por ejemplo:
lambda_func = sum_three_values(3)
my_sum2 = lambda_func(1, 2)
print(my_sum2)
# Lo que daria el mismo resultado, pero lo habriamos hecho en dos pasos separados.

""" 
Siempre que se quiera llamar a una lambda devuelta por una funcion, debemos proporcionar
los argumentos que la lambda espera entre parentesis. Si lo hacemos inmediatamente despues de
obtener la lambda, los argumentos van justo despues de los parentesis que cierran la llamada
a la funcion externa.
"""
