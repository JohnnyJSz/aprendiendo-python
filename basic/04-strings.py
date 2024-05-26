# Strings

my_string = "mi variable string"
my_string_2 = 'mi variable string 2'

print(my_string)
print(len(my_string))

print(my_string + " " + my_string_2)

my_new_line_string = '**Este es un string\ncon salto de linea**'
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

my_scape_string = "\\tEste es un string\\nescapado"
print(my_scape_string)

# formateo
nombre, apellidos, edad = "Jonathan", "Jimenez Salazar", 32
print("Mi nombre es {}, mis apellidos son {} y mi edad es de {} años.".format(nombre, apellidos, edad))
print("Mi nombre es %s, mis apellidos son %s y mi edad es de %d años." %(nombre, apellidos, edad))
miguel_name, miguel_height, miguel_age = "Miguel", 0.76, 1
print('%s is %d year old and his height is %f cm.' %(miguel_name, miguel_age, miguel_height)) # El orden aqui dentro de %() es importante
print('{} is {} year old and his height is {} cm.'.format(miguel_age, miguel_name, miguel_height)) 
# La mejor opcion - string interpolation - f string - inferencia de datos
print(f"Mi nombre es {nombre}, mis apellidos son {apellidos} y mi edad es de {edad} años.")

# Desempaquetado de caracteres
texto = "hola"
texto_2 = "abcdefghijklmno"
a, b, c, d = texto
print(texto)
print(a)
print(b)
print(c)
print(d)

# Division slicing [start:stop:step]
lenguaje_slice = texto[1:3] # selecciona las letras de la pos 1 a la 3 sin contar la 3
print(lenguaje_slice)
lenguaje_slice = texto[2:] # pos 2 hasta el final
lenguaje_slice = texto[:3] # inicio hasta la pos 3 sin contar la 3
print(lenguaje_slice)
texto_2_seleccion = texto_2[0:11:3] # Evitamos caracteres
print(texto_2_seleccion)

# Reverse
lenguaje_reversed = texto[::-1]
print(lenguaje_reversed)

# Funciones
print(texto_2.capitalize()) # La primera letra en mayuscula
print(texto_2.upper()) # pone todo en mayuscula
print(texto_2.lower()) # pone todo en minuscula
print(texto_2.count("g")) # Cuenta el num de ocurrencias del texto pasado como arg
print(texto_2.isnumeric()) # Nos dice si el texto es numerico o no
print('****',"777".isnumeric()) # Nos dice si el texto es numerico o no
print(texto_2.upper().isupper()) # Nos dice si el texto esta en mayusculas
print(texto_2.upper().islower()) # Nos dice si el texto esta en minusculas
print(texto_2.startswith("abc")) # Nos dice si el texto empieza con el sub texto del arg
print(texto_2.startswith("ABC")) # Nos dice si el texto empieza con el sub texto del arg
# Leer la documentacion para ver el resto de funciones de strings.