# Operadores aritmeticos en python
print("--- Op Aritmeticos ---")
print(1 + 4) # suma
print(1 - 4) # resta
print(1 * 4) # multiplicacion
print(1 / 4) # division

print(10 % 3) # modulo - resto de la division

print(10 / 6)
print('floor division: ',10 // 6) # 'floor division' Aproxima la division al numero entero bajo mas proximo

print(5 ** 3) # exponente - 5 elevado a 3

print("Hola" + "Python") # concatenacion de texto
print("Hola" + str(5))
print("Hola" * 3) # Repite la cadena de texto el numero de veces
print("Hola" * (3 ** 3))

print(7 * 5 + 14 - 2 / 5)

# Operadores relacionales en python
print("--- Op Comparativos ---")
print(3 > 4) # False 
print(3 < 4) # True
print(3 >= 4) # False
print(3 <= 4) # True
print(3 == 4) # False
print(3 != 4) # True
print('***',(((5 > 3) > 1) == 1)) # False
print('True::',True == 1) # True
print('True::',True == 6) # False
print('True::',True == 0) # False
print('False::',False == 1) # False
print('False::',False == 0) # False
print('False::',False == 6) # False

print('-- ',"aaa" > "aaa")
print('-- ',"aaa" < "aaa")
print('--> ',"aaa" < "aba") # Ordenacion alfabetica por ASCII
print('--> ',"aaa" < "ABA")
print('-- ',"aaa" > "AAA")
print('--> ',"hola" >= "Mundo") #True

# Operadores logicos en python
print("--- Op Logicos ---")
print(True and False)
print(True and True)
print('**>',False and False)
print(3 > 4 and 5 < 8) # False and True -> False
print(3 > 4 or 5 < 8) # False or True -> True
print(3 > 4 or (5 < 8 and 6 <= 6)) # False or (True and True) -> False or True -> True
print(not(3 > 4 or (5 < 8 and 6 <= 6))) # not(False or (True and True)) -> not(False or True) -> not(True) -> False
