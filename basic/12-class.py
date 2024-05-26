# Clases
# Las clases engloban de principio a fin un objeto, un objeto entidad que representara algo del mundo real
# Las clases envuelven toda la logica relacionada con el objeto clase
# por ejemplo, la clase persona tendra las caracteristicas y metodos propios
# del objeto en la vida real persona, andar, comer, hablar, 4 extremidades, etc..
# no tendra, por ejemplo, la habilidad de volar.

# las clases se escriben la primera letra con Mayuscula
# Si hay mas de una palabra se escribe en CammelCase en vez de snake_case
# class MyPerson:
class EmptyPerson:
  pass # Pass permite saltarnos el codigo para que no ejecute nada.
# El pass nos permite imprimir la clase vacia para ver que nos muestra
print(EmptyPerson)
print(EmptyPerson())

# Idealmente las clases irian en su propio archivo o fichero
class Person:
  # Las clases pueden tener constructores
  # __init__ es reservado del sistema, nos sirve para crear un constructor de clase

  # self siempre es requerido y es obligatorio, se refiere a la instancia de Persona
  # con self podemos crear variables de la clase y asignarles los parametros necesarios
  # estas variables despues pasaran a existir fuera de la clase, es decir, podremos
  # acceder a ellas usando la notacion punto (.)
  # en nuestro ejemplo, una instancia de Persona va a tener name y surname y tomaran los
  # valores que al crear una instancia Persona, el usuario le asigne

  # Ahora ya tendremos la capacidad que la clase Persona reciba algun parametro
  # por ejemplo un nombre y apellido
  def __init__(self, name, surname, alias = 'sin alias') -> None:
    # self.name = name # propiedades publicas
    # self.surname = surname
    self.full_name = f'{name} {surname} ({alias})'
    # con __ decimos que las propiedades son privadas, solo se podrian acceder o modificar mediante getters o setters
    self.__name = name

  # Para hacer un getter creamos una funcion que devuelva lo que deseamos
  def get_name(self):
    return self.__name
  
  # Podemos añadir funciones a la clase
  def talk (self):
    print(f'{self.full_name} está hablando')

# Usamos la clase y creamos una instancia de Person
miguel = Person("Miguel", "Jimenez Sanchez")
print(f'Mi hijo se llama {miguel.full_name}')
miguel.talk()

jonathan = Person("Jonathan", "Jimenez Salazar", "Telito")
print(f'Yo me llamo {jonathan.full_name}')
jonathan.talk()

random_person = Person("Random", "Randomes")
# print('acceder a una prop privada : erroneamente -',random_person.__name) # No podemos acceder directamente, necesitamos una funcion getter para ello
print('acceder a una prop privada : correctamente -',random_person.get_name())
print(random_person.full_name)

# Podemos cambiar el valor de una propiedad reasignandole un nuevo valor
# como si de una variable normal se tratase
random_person.full_name = "Ramiro Romero (El Romano)"
print(random_person.full_name)

# Ademas podemos cambiar completamente el valor y el tipo de dato
# gracias al tipado debil del lenguaje
random_person.full_name = 666
print(random_person.full_name)