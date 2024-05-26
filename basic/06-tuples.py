# Tuplas - Tuples
# Las tuplas son un conjunto de valores

my_tuple = tuple()
my_other_tuple = ()

print(my_tuple)
print(my_other_tuple)
print(type(my_tuple))
print(type(my_other_tuple))

x = (1,'hola',4.4,['a',False])
y = list('abc')
print(x)
print(y)

my_tuple = ('blanco', 'gris', 'negro', 'gris')
my_other_tuple = (1, 2, 3, 4)

print(my_tuple)

# seleccionar elementos
print('el pos 2 -',my_tuple[2])
print('el ultima pos -',my_tuple[-2])
# print('fallo al acceder al el en la pos -',my_tuple[4]) #indexError

print('cuenta los elementos \'gris\' en la tupla -',my_tuple.count('gris'))
print('nos devuelve el indice del elemento \'gris\' en la tupla -',my_tuple.index('gris')) # El primer indice que encuentra


# Las tuplas son inmutables, no se puede reasignar valores
# my_tuple[1] = 'verde'
# print(my_tuple) # typeError - No se puede reasignar valores en una tupla
# my_tuple[5] = 'morado'
# print(my_tuple) # typeError - 'tuple' object does not support item assignment - No se puede reasignar valores en una tupla ni añadir mas valores

# La tupla ha cambiado, las hemos concatenado
print(my_tuple + my_other_tuple)
# podemos asignar el valor de la nueva tupla en una variable
my_concat_tuple = my_tuple + my_other_tuple
print(my_concat_tuple)
print('%^%^%',my_concat_tuple[3:6])

# Borrar
# del my_concat_tuple[2]
# print(my_concat_tuple) TypeError: 'tuple' object doesn't support item deletion
# del my_concat_tuple
# print(my_concat_tuple) # NameError: name 'my_concat_tuple' is not defined.