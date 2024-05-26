# Sets
# Un set tiene de base un array, aunque en Python no hay arrays como tal.
# Un set no es una estructura ordenada, ordena los elementos por un hash interno
# Su forma de guardar elementos es desordenada
# Un set no admite elementos repetidos

my_set = set()
my_set_2 = {}

print(type(my_set))
print(type(my_set_2)) # dict? que pasa aqui?

my_set_2 = {"rojo", "azul", "amarillo"}

print(type(my_set_2)) # set? wow que paso?

""" Un diccionario y un set se pueden definir de la misma forma
usando {}. La variable cambiara a set cuando tenga valores 
"""

print(len(my_set_2)) # Longitud del set con 3 elementos

# Acceder a los elementos
# print(my_set_2[0]) #TypeError: 'set' object is not subscriptable

my_set.add("uno")
my_set.add("dos")
my_set.add("tres")
print(my_set)
my_set.add("cuatro")
print(my_set)
my_set.add("tres")
print(my_set)

print("uno" in my_set) # Asi compobramos que un elemento existe dentro de mi set
print("siete" in my_set)

my_set.remove("uno")
print(my_set)

# my_set.clear() # Borra todos los elementos de nuestro set pero el set sigue creado
# print(my_set)

# del my_set # Borra el objeto por completo
# print(my_set) # NameError: name 'my_set' is not defined.

my_set_3 = {"javascrip", "python", "java"}
my_set_4 = {"html", "css"}
my_comb_set = my_set_3.union(my_set_4)
print(my_comb_set)
print(my_comb_set.union(my_comb_set)) # No pasa nada por que los elementos en los set no se duplican

print(my_comb_set.difference(my_set_4)) # Muestra los elementos que son diferentes a los dos sets

""" Hay mas metodos que vamos a ir descubriendo mirando
la documentacion y jugando con ellos. 
"""

l = ['hola','mundo']
set1 = set(['hola','mundo'])
# set1 = {1,3,2,5,4}
for el in set1:
  print(el)


mi_conjunto = {1, 2, 3}
mi_conjunto.add(4)
print(mi_conjunto)

my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
print(my_set)

mi_conjunto = {1, 2, 3, 4, 5}
mi_conjunto.discard(3)
print('t',mi_conjunto)
mi_conjunto = {1, 2, 3, 4, 5}
mi_conjunto.discard(99)
print('t',mi_conjunto)

my_set = set([1, 2,3,4])
deleted_element = my_set.pop()
print(deleted_element)

s = set([1, 2])
s.clear()
print(s) #set()

s_a = {1, 2, 3, 4}
s_b = {3, 4, 5, 6}
s_diff = s_a.difference(s_b)
print('***',s_diff)
s_1 = {'c', 'o', 's', 'a'}
s_2 = {'s', 'a', 'c', 'o'}
s_diff2 = s_1.difference(s_2)
print('***',s_diff2)

conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}
conjunto_interseccion = conjunto_a.intersection(conjunto_b)
print(conjunto_interseccion)