# Manejo de Excepciones o errores
# Si nuestro programa da un error y nosotros no controlamos eso, la app se rompe.
# para evitar eso debemos controlar los errores / excepciones
# para ello tendremos una serie de mecanismos para mitigar los errores.

""" try:
  ejecuta el codigo
except: # puede o no tener una condicion
  ejecuta este codigo cuando hay una excepcion o error
else:
  no hay excepciones? se ejecuta este codigo.
finally:
  Siempre ejecuta este codigo. 
"""

# try:
#   num1 = input('Introduce un numero: ')
#   num2 = input('Introduce otro numero: ')
#   print(type(num1)) # comprobamos que nuestro numero es de tipo str
#   print(type(num2)) # comprobamos que nuestro numero es de tipo str
#   print(f'La suma de {num1} y {num2} es: ',int(num1) + int(num2))
# except:
#   print('Ha habido un error')
# else:
#   print('La suma se ha podido hacer')
# finally:
#   print('proceso de suma finalizado.')

# Excepciones por tipo
# TypeError
number1 = 4
number2 = "1"
# print(number1 + number2)
# Al ejecutar el codigo anterior puedo ver en consola que 
# es del tipo TypeError
# Hay mas tipos q TypeError, por ejemplo ValueError
# con lo cual ahora sabiendo eso, puedo manejar
# errores mas personalizados segun el tipo

try:
  print(number1 + number2)
  print('No ha habido error')
except ValueError:
  print('ValueError: Ha habido un error del tipo ValueError')
except TypeError:
  print('TypeError: Ha habido un error del tipo TypeError')
# si queremos capturar todos los errores simplemente usamos except:

# Captura de la informacion de la excepcion
try:
  print(number1 + number2)
  print('No ha habido error')
except TypeError as my_error: # my_error se puede llamar como queramos, los mas comunes son error o e, es el nombre de la variable que contiene la info del error.
  print('my error capturado',my_error)
except Exception as my_error: # Es una excepcion generica, en caso de que no sea TypeError, se va por aqui
  print('my error capturado',my_error)

