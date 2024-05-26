# Diccionarios
# conjunto de relaciones clave valor
# tip: se llama diccionario por que si busco por la clave X, me va a dar su valor Y
# { x: y }

my_dict = dict()
my_dict_2 = {}

print(type(my_dict))
print(type(my_dict_2))

my_dict = {
  "nombre": "jonathan",
  "apellidos": "jimenez salazar",
  "edad": 32,
  "lenguajes": {
    "javascript",
    "react",
    "python"
  }
}

print(my_dict)
print(len(my_dict)) # 4 claves raiz tiene my_dict

print('**',my_dict["apellidos"]) # Nos muestra el valor de la clave pasada entre corchetes
my_dict["apellidos"] = 'sanchez crespo'
print(my_dict["apellidos"])
my_dict["calle"] = "Calle Falsa 123"
print(my_dict["calle"])
print(my_dict)
print(len(my_dict))

# metodos
# Podemos eliminar un elemento de nuestro dic usando del
del my_dict["calle"]
print(my_dict)

# comprobar si hay algo en my_dict
print("nombre" in my_dict) # True - Las claves si las hay, devuelve true
print("jonathan" in my_dict) # False - los valores no los comprueba, aunque los haya.

print('.items -',my_dict.items()) # listado con cada uno de los items (key value) del dict
print('.keys -',my_dict.keys()) # listado de las keys del dict
print('.values -',my_dict.values()) # listado de los valores del dict

my_new_dict = dict.fromkeys(("Key1", "Key2", "")) # Crea un diccionario nuevo con keys especificos pero sin valores
print(my_new_dict) 

# Crear un dict con keys a partir de una lista, pero sin valores.
my_list = ["uno", "dos", "tres"]
my_new_dict_2 = dict.fromkeys(my_list)
print(my_new_dict_2)

# Crear un dict con fromkeys a partir de otro dict y dando values como segundo arg de fromkeys
my_new_dict_3 = dict.fromkeys(my_dict, ("hola"))
print(my_new_dict_3)

print(list(my_new_dict_3))
print(tuple(my_new_dict_3))
print(set(my_new_dict_3))


mi_diccionario = {'nombre': 'John', 'edad': 30, 'ciudad': 'New York'}

# Mostrar todos los valores usando values()
for valor in mi_diccionario.values():
    print(valor)

# Acceder a un valor específico por clave
print(mi_diccionario['edad'])

print(mi_diccionario.values())


d = {'nombre': 'John', 'edad': 30}

# Acceder a un elemento
print('1',d['nombre'])


# Modificar un elemento
d['edad'] = 31
print('2',d['edad'])


# Agregar un nuevo par clave-valor
d['ciudad'] = 'New York'
print('3',d.get('ciudad'))


# Uso de get para acceder a un valor con clave inexistente
print(d.get('profesion', 'No especificado'))  # Muestra 'No especificado' por defecto
