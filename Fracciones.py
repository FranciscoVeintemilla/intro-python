


class Fraccion:
    '''
    La clase fraccion permite crear objetos de tipo fraccion
    '''


    def __init__(self, numerador, denominador):
        self._numerador = numerador
        self._denominador = denominador


    def __str__(self):
        return f'Fraccion {self.__dict__.__str__()}'


    @property
    def numerador(self):
        return self._numerador

    @numerador.setter
    def numerador(self, numerador):
        self._numerador = numerador

    @property
    def denominador(self):
        return self._denominador

    @denominador.setter
    def denominador(self, denominador):
        self._denominador = denominador

if __name__ == '__main__':
    f1 = Fraccion(4,5)
    print(f1)
    f1.numerador = 5
    print(f1)
    f1.denominador = 6
    print(f1)
    f1._numerador = 7
    print(f1)


