# Listas
# Estructura mas flexible que un array para trabajar con datos.
# La lista es como una caja en la que vamos añadiendo elementos

my_list_1 = list()
my_list_2 = []
my_list_3 = []

print('--',my_list_1)
print('--',my_list_2)

print('Longitud: ',len(my_list_1)) # longitud de la lista
print('Longitud: ',len(my_list_2))

my_list_1 = [23, 4, 5, 12, 1, 3, 5, 33, 24, 4, 5, 11, 12, 1, 20]
my_list_2 = ['oso', 'perro', 'gato', 'vaca', 'conejo', 12.5, 4, False, True, 77, 'leon', 'lobo', False, 66, 1]
my_list_3 = ['oso', 'perro', 'gato', 'vaca', 'conejo', 43, 55, 23, 24, 55]
my_list_4 = ['amarillo', 'azul', 'rojo', 'verde']
print('Longitud: ',len(my_list_1))
print('Longitud: ',len(my_list_2))

print(type(my_list_1))
print(type(my_list_2))

l = [1,2,3,4,5]
l[8]
print('--->',l[3])
# seleccionar elementos de la lista en base al indice
print(my_list_1[0]) # primer elemento
print(my_list_1[-1]) # ultimo elemento
print(my_list_1[-4]) # el 4to elemento empezando por el final
print(my_list_1.count(5)) # cuenta las ocurrencias del elemento pasado como arg

# Desempaquetar una lista
# animal1, animal2, animal3 = my_list_2
# print(animal1) # error, intentamos desempaquetar toda la lista de 15 elementos en 3 elementos.
oso, perro, gato, vaca, conejo, osoNum, perroNum, gatoNum, vacaNum, conejoNum = my_list_3
print(oso, osoNum, perro, perroNum)

rojo, azul, verde, amarillo = my_list_4[2], my_list_4[1], my_list_4[3], my_list_4[0]
print(rojo, azul, verde, amarillo)

# sumar / concatenar listas 
print(my_list_3 + my_list_4)

# Añadir un nuevo elemento a la lista
my_list_4.append('negro')
print(my_list_4)

# Añadir en una posicion concreta
my_list_4.insert(0,'morado')
print(my_list_4)

# Quitar elementos que sabemos que existen
my_list_4.remove('rojo') # elimina el elemento rojo
my_list_3.remove(55) # Si hay mas de una ocurrencia solo elimina la primera.
print(my_list_4)
print(my_list_3) 

print(my_list_4)
# desapila o elimina el ultimo elemento de la lista y devuelve el elemento eliminado
# print('.pop() elemento -',my_list_4.pop())
print('.pop() elemento -',my_list_4.pop(1)) # indice del elemento a desapilar
print('.pop() lista -',my_list_4)

# Eliminar por indice
print('eliminar por indice: ',my_list_4)
del my_list_4[2] #Elimina el elemento del indice 2, es decir, 'verde'
print('eliminar por indice: ',my_list_4)

# Modificar un valor
my_list_4[1] = 'marron'
print(my_list_4)

# Copiar lista
copy_my_list_4 = my_list_4.copy()
print('copia de my_list_4 -',copy_my_list_4)

# Revertir la lista
copy_my_list_4.reverse()
print('dar la vuelta a la lista -',copy_my_list_4)

# Ordenar la lista en orden alfabetico
copy_my_list_4.sort()
print('lista ordenada -',copy_my_list_4)

# Sub listas
print('sub listas -',copy_my_list_4[0:2])

# borrar lista entera
my_list_4.clear()
print('my_list_4 borrada -',my_list_4)

# tipado dinamico, si reasigno la variable a una string obtengo una variable de tipo string
my_list_1 = "Hola python"
print(type(my_list_1))