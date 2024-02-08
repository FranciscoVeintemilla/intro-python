# #definicion de funciones
# # se utliza la sintaxis def nombre_funcion(parametros): identacion del bloque de codigo
# def saludar():
#     print(f'Habla')
#
# saludar()
#
# def saludar_nombre(nombre, apellido):
#     print(f'habla {nombre.capitalize()} {apellido.capitalize()}')
#
# saludar_nombre('Francisco', 'Perez')
#
# def suma(sumando1, sumando2):
#     resultado = sumando1 + sumando2
#     return resultado
#
# r = suma(5, 10)
# print(r)
#
# def escoger_modulo(modulo):#modulo puede ser un modulo 1 o modulo 2
#     if modulo == 1:
#         return f'modulo Uno ({modulo})'
#     elif modulo==2:
#         return f'modulo Dos'
#     else:
#         return f'Modulo equivocado'
#
# print (escoger_modulo(3))
#
# modulo = int(input('ingrese el modulo 1 o 2: '))
#
# print(escoger_modulo(modulo))


# def definir_genero(genero): # el genero puede ser 'F' o 'M'
#     if genero == 'F':
#         return 'Femenino'
#     elif genero == 'M':
#         return 'Masculino'
#     else:
#         return 'Genero equivocado'
#
#
# genero = input('Ingrese el genero (F o M): ')
#
# print(definir_genero(genero.upper()))

# def registrar(nombre, apellido, cedula=None):
#     if cedula:
#         return f'{nombre.capitalize()}  {apellido.capitalize()} - {cedula}'
#     else:
#         return f'{nombre.capitalize()} {apellido.capitalize()}'
#
# print(registrar(apellido='Perez', cedula='0928164870', nombre='Francisco'))
# print(registrar('perez', '0929281640', 'Francisco'))
# x = input('nombre(*): ')
# y = input('apellido(*): ')
# z = input('Cedula: ')
# # print(registrar(nombre, apellido, cedula))
# print(registrar(nombre=x, cedula=z, apellido=y))
# # print(registrar(nombre=x, apellido=y))

def registrar2(*args):
    print(f'cantidad de argmentos:  {len(args)}')
    for argumento in args:
        print(argumento)
    # return f'{nombre.capitalize()} {apellido.capitalize()}'

# x = input('nombre(*): ')
# y = input('apellido(*): ')

print registrar2(*args:'luis', 'Perez', '0258', 'lperez@gmail.com', ))