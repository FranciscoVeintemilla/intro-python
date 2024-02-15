from persona import Persona

class Empleado(Persona):
    def __int__(self, nombre, cedula, genero, ocupacion, sueldo):
        Persona.__int__(nombre=nombre, genero=genero, ocupacion=ocupacion, cedula=cedula)
        self._sueldo = sueldo

    def __str__(self):
        return f'Empleado[ sueldo: {self._sueldo}], {super().__str__()}]'

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

if __name__=='__main__':
    e1 = Empleado('Carlos', '0929281640', 'M', 'Profesor')
    print(e1)
    e1.cedula = '0984415215'
    print(e1)