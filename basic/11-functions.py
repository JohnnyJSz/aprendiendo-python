# Funciones

# para definir una funcion usamos la palabra reservada deg y el nombre de nuestra funcion
def my_function():
  print('my primera funcion')

my_function()

# parametros o argumentos de una funcion
def sum_two_nums(first_number, second_number):
  print(first_number + second_number)

sum_two_nums(15, 5)
sum_two_nums(41123, 5131)
sum_two_nums(1, 0)

# El tipado no funciona del todo en este caso, ya que Python es de tipado debil y dinamico
# def sum_two_values(value1: int, value2: int):
#   print(value1 + value2)
# sum_two_values("hola", "mundo") # -> holamundo

def sum_two_values_num_with_return(num1, num2):
  sum = int(num1) + int(num2)
  return sum
sum_result = sum_two_values_num_with_return("5", "2")
print(sum_result)
print(sum_result + 8)

def print_name(name, surname):
  print(f'Mi nombre es {name} y mi apellido es {surname}')

print_name("Jimenez", "Miguel")
# En este punto, mi funcion funciona bien pero al introducir los datos
# El usuario los ha puesto en el orden equivocado, como podemos, de algun
# manera solucionar esto, indicando en la llamada de la funcion
# los argumentos y su valor.
print_name(surname="Jimenez", name="Miguel")

# parametros por defecto
def print_name_with_default(name, surname, alias = "Sin alias"):
  print(f'with default: Mi nombre es {name}, mi apellido es {surname} y mi alias es {alias}')

print_name_with_default("Miguel", "Jimenez", "Chiquito")
print_name_with_default("Miguel", "Jimenez")

# Parametros indefinidos
# usando * en el argumento le indicamos que vamos a poder pasarle los argumentos que
# queramos a nuestra llamada de la funcion.
# internamente al argumento lo interpreta como una tupla
def print_texts(*text):
  print(text)

print_texts()
print_texts("hola mundo!")
print_texts("hola mundo!", "Me gusta aprender python", "Mi hijo se llama Miguel")

def print_texts_in_upper(*texts):
  print(type(texts))
  for text in texts:
    print(text.upper())

print_texts_in_upper("hola mundo!", "Me gusta aprender python", "Mi hijo se llama Miguel")

# Se pueden hacer mas cosas, hay que mirar la documentacion
# para profundizar mas en las funciones.