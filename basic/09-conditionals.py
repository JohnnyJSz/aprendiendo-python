# Condicionales
# Sirven para establecer flujos de ejecucion de nuestro codigo
# decidir si algo se va a ejecutar o no.

""" Un condicional cumple la siguiente formula 
Si se cumple una condicion, ejecuta lo que esta dentro
del bloque condicional
"""

my_condition = False

# if my_condition == True:
if my_condition:
  print('Se ejecuta el 1er bloque condicional')

my_condition = 5 * 5

if my_condition == 10:
  print('Se ejecuta el 2do bloque condicional')

if my_condition > 10:
  print('Se ejecuta el 3er bloque condicional')

# y si quiero hacer algo cuando la condicion no se cumple? podemos usar el ELSE
if my_condition > 10:
  print('Es mayor que 10')
else:
  print('Es menor o igual que 10')


if my_condition > 10 and my_condition < 20:
  print('Es mayor que 10 y menor que 20')
elif my_condition == 25:
  print('Es igual a 25')
else:
  print('Es menor o igual que 10 o mayor o igual que 20 o distinto de 25')

my_string = 'Mi cadena de texto'

if my_string:
  print("Mi cadena de texto no es vacia")
if my_string == 'Mi cadena de textooo':
  print("Mis cadenas de texto coincide")
else:
  print("Mis cadenas de texto no coinciden")

my_string_2 = ""
if not my_string_2: # my_string_2 es "" con lo cual es igual a False. Al añadir not se convierte a True
  print('Mi cadena de texto es vacia')


print('La ejecucion continua')