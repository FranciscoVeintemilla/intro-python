
class Persona:
    '''
    crear los objetos de tipo Persona
    '''
    def __init__(self, nombre, genero, ocupacion, cedula): #metodo que incializa al objeto de tipo persona (constructor)
        self._nombre = nombre
        self._genero = genero
        self._ocupacion = ocupacion
        self._cedula = cedula

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def genero(self):
        return self.genero

    @genero.setter
    def genero(self, genero):
        self._genero = genero

    @property
    def ocupacion(self):
        return self.ocupacion

    @ocupacion.setter
    def ocupacion(self, ocupacion):
        self._ocupacion = ocupacion

    @property
    def cedula(self):
        return self.cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

        #agregar un nuevo atributo cedula
        #encapsular todos los atributos con los decoradores

    def __str__(self): #downders son sobre escritos
         return (f'Persona: [nombre: {self._nombre}, genero: {self._genero}, '
                 f'ocupacion: {self._ocupacion}, cedula: {self._cedula}')

    def saludar(self):
        print(f'Hola soy {self._nombre}')

if __name__ == '__main__':
    obj_persona1 = Persona('Carlos', 'M', 'Ninja', '0929211144')
    print(obj_persona1.__str__())
    obj_persona2 = Persona(genero='M', ocupacion='Estudiante', nombre='Luis', cedula='135190155')
    print(obj_persona2)
    p3 = Persona(nombre='Jose', genero='M', cedula='0929281160', ocupacion='Ladron')
    print(p3)
    obj_persona1.saludar()
    #p3.cedula = '010201111'
    print(p3)


