# Variables

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 7
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

# Print puede tener multiples argumentos - funciones incorporadas
print('-string variable:', my_string_variable, '-int variable:', my_int_variable, '-bool variable:', my_bool_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable, type(my_int_to_str_variable))

# longitud - funciones incorporadas
print(len(my_string_variable))

# Variables en una sola linea
nombre, apellidos, edad, altura = "Jonathan", "Jimenez Salazar", 32, 1.75
print('My nombre es',nombre,"mi apellido es",apellidos,"mi edad es",edad,"y mi altura es",altura,"cm.")

# inputs por parte del usuario - funciones incorporadas
new_age = input("Que edad tienes: ")
print("Tu edad es",int(new_age))

# reasignacion de tipo de variable
new_age = "un dos tres"
print('El nuevo tipo de new_age es: ',new_age,type(new_age))

# asignacion explicita de tipo de variable?
address: str = "new road 123"
print(address, type(address))
address = 5
print(address, type(address))
# Tipado debil