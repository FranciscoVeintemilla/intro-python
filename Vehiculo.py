class Vehiculo:
    '''
    Crear los objetos de tipo Vehiculo
    '''
    def __init__(self, marca, modelo, pais, ano_construccion): # Método que inicializa al objeto de tipo vehiculo
        self._marca = marca
        self._modelo = modelo
        self._pais = pais
        self._ano_construccion = ano_construccion

    def __str__(self):
        return (f'Vehiculo: [marca: {self._marca}, modelo: {self._modelo}, '
                f'pais: {self._pais}, ano de construccion: {self._ano_construccion}')

    def describir(self):
        print(f'Este es un {self._marca} {self._modelo} construido en {self._pais} en el año {self._ano_construccion}')

if __name__ == '__main__':
    obj_vehiculo1 = Vehiculo('Toyota', 'Corolla', 'Japon', 2020)
    print(obj_vehiculo1.__str__())
    obj_vehiculo2 = Vehiculo(marca='Ford', modelo='Mustang', pais='Estados Unidos', ano_construccion=1965)
    print(obj_vehiculo2)
    v3 = Vehiculo(marca='Renault', modelo='Clio', pais='Francia', ano_construccion=2005)
    print(v3)
    obj_vehiculo1.describir()
