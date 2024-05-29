# Higher Order Functions

""" 
Las funciones de orden superior en Python son funciones que pueden hacer 
una de las siguientes cosas (o ambas)
- Recibir funciones como argumentos: pasar funciones como argumentos a las otras funciones
- Devolver funciones: pueden devolver una funcion como resultado.

Esto es posible porque en Python las funciones son "ciudadanos de primera clase", lo que 
significa que se pueden tratar como cualquier otro objeto (asignarlas a variables, pasarlas como argumentos, etc.)
"""
# Ejemplo 1
# definir unas funciones y usar una de ellas dentro de la funcion principal otra
def sum_one(value):
  return value + 1
def sum_five(value):
  return value + 5

def sum_two_values_and_add_another_function(value1, value2, f_sum):
  return f_sum(value1 + value2)

print(sum_two_values_and_add_another_function(5, 2, sum_one))
print(sum_two_values_and_add_another_function(5, 2, sum_five))

# Ejemplo 2
# Funcion que devuelve funcion
def creador_multiplicador(n):
  def multiplicar(x):
    return x * n
  return multiplicar

multiplicar_por_3 = creador_multiplicador(3)
print(multiplicar_por_3(10))
# La funcion creador_multiplicador devuelve una nueva funcion que multiplica su argumento por 'n'


# Closures
""" 
Una Closure (o clausura) en Python es una funcion definida dentro de otra funcion que recuerda el
entorno en el que fue creada, es decir, puede acceder a las variables locales de la funcion contenedora
incluso despues de que esta haya finalizado su ejecucion

Componentes de un Closure
- Una funcion interna: la funcion que se define dentro de otra funcion
- Variables libres: variables que no son locales ni globales, sino que estan definidas en el
  entorno de la funcion contenedora.
- El entorno: el contexto en el que se define la funcion interna.
"""
# Ejemplo 1
def sum_ten():
  def add(value):
    return value + 10
  return add

add_closure = sum_ten() # Retorna una funcion que la almacenamos en una variable
print(add_closure(5)) # Imprimimos el resultado de esa variable funcion

# Ejemplo 2
def sum_ten_plus_value(original_value):
  def add(value):
    return value + 10 + original_value
  return add

print(sum_ten_plus_value(5)(1)) #La funcion con un valor (original_value = 5) retorna una funcion que despues invocamos con un nuevo valor (value = 1)


# Built-in Higher Order Functions
numbers = [2,5,10,21,3,30]

# Map
def multiply_two(number):
  return number * 2

print(list(map(multiply_two, numbers)))
# se podria usar una lambda en vez de definir la funcion
print(list(map(lambda num: num * 2, numbers)))

# Filter
def filter_greater_than_ten(number):
  if number > 10:
    return True
  else:
    return False
  
print(list(filter(filter_greater_than_ten,numbers)))
print(list(filter(lambda number: number > 10,numbers)))

# Reduce
from functools import reduce

def sum_two_values(value1, value2):
  return value1 + value2

# Reduce empieza con los 2 primeros valores de numbers, los suma y el resultado lo usa como
# value1 en la siguiente iteracion o mejor dicho, para el siguiente elemento en numbers
# numbers = [2,5,10,21,3,30]
# el empezar v1 y v2 = 2 y 5 => 7
# v1, v2 = 7, 10 => 17
# v1, v2 = 17, 21 => 38
# v1, v2 = 38, 3 => 41
# v1, v2 = 41, 30 => 71 Resultado final.
print(reduce(sum_two_values,numbers))