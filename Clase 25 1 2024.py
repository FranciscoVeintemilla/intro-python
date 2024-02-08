# colores = ('rojo', 'azul', 'amarillo', 'azul')
# print(colores)
# print(type(colores))
# print(len(colores))
#
# tupla1 = (1)
# print(type(tupla1))
# tupla2 = (1,)
# print(type(tupla2))
# print(colores[2])
#
# if "rojo" in colores:
#     print("si esta el color rojo")
# else:
#     print("no esta el color rojo")
#
# # colores.insert(2,'negro')
# # colores[0] = 'negro'
# # print(colores)
#
# #se convierte la tupla a una lista
# lista = list(colores)
# print(type(lista))
# #cambiando el elemento del indice 1
# lista[1] = 'negro'
# colores = tuple(lista)
# #convierto la lista en tupla
# colores = tuple(lista)
# print(colores)
# print(type(colores))

###################################################
#######conjuntos - set
###################################################
marcas = {'sony', 'prima', False, 'samsung', 'prima', 'sony', True, 1}
print(marcas)
print(type(marcas))
print(len(marcas))
materias = set
materias.add('LPP')
print(materias)

for item in marcas:
    print(item)

marcas2 = {'panasonic', 'tcl', 'sony'}
marcas.update(marcas2)
print(marcas)




