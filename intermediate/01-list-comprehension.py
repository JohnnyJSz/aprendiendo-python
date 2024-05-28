# List Comprehension
""" 
List Comprehension
  Es una forma concisa y eficiente de crear listas en Python. 
  Permite generar una nueva lista aplicando una expresion a cada elemento 
  de una secuencia, como una lista, tupla o rango.

  Sintaxis basica
    nueva_lista = [expresión for elemento in iterable]
"""
my_original_list = [0,1,2,3,4,5]

# Algo que llamaremos 'el', que va a ser cada uno de los elementos 'el' en la lista my_original_list
my_list = [el for el in my_original_list]
# Esto transforma una lista en otra lista
# Si ya tenemos una lista, sirve para hacer cosas con esa lista o si no tenemos lista, para crear una
print(my_list)

# usando rango. para crear listas con rango definido
my_list2 = [el for el in range(21)]
print(my_list2)

# es lo mismo que hacer
my_range = range(21)
my_list3 = list(my_range)
print(my_list3)

# Si quisieramos crear una lista y hacer una operacion sobre ella podemos usar el for in
# sumar, restar, multiplicar, usar funciones, etc...
my_list4 = [el + 10 for el in range(11)]
print(my_list4)

my_list5 = [el * 2 for el in range(11)]
print(my_list5)

my_list6 = [el * el for el in range(11)]
print(my_list6)

def sum_five(number):
  return number + 5
my_list7 = [sum_five(el) for el in range(6)]
print(my_list7)

# Ejemplo practico:
# Supongamos que queremos crear una lista de los cuadrados de los numeros del 1 al 5.
# SIN LIST COMPREHENSION
cuadrados_no_lc = []
for numero in range(0, 6):
  cuadrados_no_lc.append(numero ** 2)
print('Cuadrados SIN list comprehension: ',cuadrados_no_lc)
# CON LIST COMPREHENSION
cuadrados_lc = [numero ** 2 for numero in range(6)]
print('Cuadrados CON list comprehension: ',cuadrados_lc)

""" 
Con condiciones
Se pueden agregar condiciones para filtrar los elementos que queremos incluir en la nueva lista
Las ventajas de esto es que es:
  conciso: reduce la cantidad de codigo necesario.
  legible: hace que el codigo sea mas facil de entender
  eficiente: generalmente mas rapido que construir una lista con un bucle 'for' estandar
Ejemplo practico:
Queremos una lista de los cuadrados de los numeros del 1 al 10, pero solo los numeros pares 
"""
cuadrados_lc_pares = [num ** 2 for num in range(1, 11) if num % 2 == 0]
print('Cuadrados de los num PARES del 1 al 10 CON list comprehension: ',cuadrados_lc_pares)

# Otro ejemplo
# Crear una lista de caracteres de una cadena:
characters = [char for char in 'Python']
print(characters)

# Convertir una lista de grados Celsius a Fahrenheit:
celsius = [0, 10, 20, 25, 30, 37.5, 39]
celsius_to_fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print(celsius_to_fahrenheit)