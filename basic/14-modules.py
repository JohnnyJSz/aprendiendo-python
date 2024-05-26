# Modulos

# Un modulo es similar al concepto de libreria en otros frameworks
# Codigo externo a nuestro fichero que queremos utilizar
# con lo cual vamos a tener que importarlo

# para acceder a otros ficheros usamos la palabra import
import module

module.sumValues(5,2,3)
module.printName("Miguel")

# Ademas podemos importar elementos concretos
from module import printName, sumValues
printName("Sara")
sumValues(0, 3, 2)

# Modulos de python
from math import pi as numero_pi
from math import pow as potencia

PI_VALUE = numero_pi

print(f'El numero pi es {PI_VALUE}')
print(f'5 elevado a 3 es {potencia(5,3)}')