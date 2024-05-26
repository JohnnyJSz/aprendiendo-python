# Loops
# Es un mecanismo para iterar
# pasar por un mismo codigo varias veces.

# While, opcionalmente puede aceptar el bloque else para casos concretos de salida explicita del bucle.
my_condition_1 = 1

while my_condition_1 <= 10:
  print('Comienza el bucle')
  print(f'my_condition tiene valor {my_condition_1}')
  # my_condition = my_condition + 1
  my_condition_1 += 1
  print(f'my_condition_1 tiene valor {my_condition_1} despues del incremento')
else: # es opcional
  print('else: my_condition_1 es mayor que 10')

while my_condition_1 < 20:
  print(f'my_condition_1 tiene valor {my_condition_1}')
  if my_condition_1 == 15:
    print('my_condition_1 es igual a 15')
    print('usando el break se detiene la ejecucion')
    break
  my_condition_1 += 2


# For
# Nos sirve para iterar un listado de elementos
# se ejecuta tantas veces como elementos haya en la lista
my_list = [1,2,3,4,5]
for element in my_list:
  print(f'elemento {element} en my_list')

my_tuple = ("uno", "dos", "tres", "cuatro", "cinco")
for element in my_tuple:
  print(f'elemento {element} en my_tuple')
  if element == "tres":
    print(f'termina la ejecucion de la iteracion para el elemento {element}')
    continue # parecido al break pero en vez de detener la ejecucion de todo el bucle, solo detiene la ejecucion de la iteracion actual, saltando a la siguiente iteracion
  print(f'final de la iteracion para el elemento {element}')

my_set = {1, 2, 3, 4, 5}
for element in my_set:
  print(f'elemento {element} en my_set')
  if element == 3:
    print(f'el elemento {element} es igual a 3')
    break # termina la ejecucion del bucle, 

my_dict = {"uno":1, "dos":2, "tres":3, "cuatro":4, "cinco":5}
for element in my_dict:
  print(f'elemento key {element} en my_dict') # Imprime las keys
  if element == "tres":
    print(f'el elemento {element} es igual a \'tres\'')
    break
for element in list(my_dict.values()):
  print(f'elemento value {element} en my_dict') # Imprime las values


print('La ejecucion continua')
