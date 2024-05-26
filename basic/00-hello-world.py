# Esto es un comentario de linea Hola Mundo
""" Esto es un 
comentario en varias lineas 
"""

print("Hola Mundo")

#----
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero.")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Ejecución finalizada.")

try:
  # Intento de operación que podría fallar
  resultado = 10 / 0
except Exception as general_exception:
  print(f"Ocurrió un error: {general_exception}")