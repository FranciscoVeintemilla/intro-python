# a = True
# print(a)
# print(type(a))
#
# bandera = False
#
# bandera = 3 < 4
# print(bandera)
#
# a = int(input('ingrese el primer numero para la operacion: '))
# b = int(input('ingrese el primer numero para la operacion: '))
# # print(type(a))
# # print(type(b))
# suma = a + b
# resta = a - b
# multiplicacion = a * b
# division = a / b
# residuo = a % b
# print(f'el resueltado de la suma de {a} y {b} es: {suma}')
# print(f'el resueltado de la resta de {a} y {b} es: {resta}')
# print(f'el resueltado de la multiplicacion de {a} y {b} es: {multiplicacion}')
# print(f'el resueltado de la division de {a} y {b} es: {division} '
#       f'y el tipo de dato es {type(division)}')
# print(f'el resueltado de la operacion residuo de {a} y {b} es: {residuo} '
#       f'y el tipo de dato es {type(residuo)}')

# # Solicita un número entero al usuario
# n = int(input("Ingrese un número: "))
#
# # Comprueba si el número es par o impar
# if n % 2 == 0:
#     print(n, "es par.")
# else:
#     print(n, "es impar.")
#
# x = 0
# x = x + 1
# print(x)
# x+=1 # lo mismo x=x+1
# print(x)

###################################################
#listas
###################################################
# frutas = ['manzana', 'naranaja', 'pera', 'naranja']
# digitos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
# direccion = ['quito', 5, True, True]
#
# print(len(frutas))
# print(len(digitos))
# print(len(direccion))
#
# print(frutas[0])
# print(frutas[2])
# print(frutas[3])
# print(frutas[-3])
#
# frutas[1] = 'sandia'
# print(frutas)
#
#
# if 'pera' in frutas:
#     print('pera esta dentro de frutas')
#
# frutas.append('uva')
#
# if 'uva' in frutas:
#     print('uva esta dentro de frutas')
# print(frutas)
#
# frutas.insert(_index:0,_object: 'piña')
# print(frutas)
#
# frutas.insert(_index:3,_object 'mandarina')
# print(frutas)
#
# frutas.remove('sandia')
# print(frutas)
#
# frutas.pop(5)
# print(frutas)

datospersonales = []
print(datospersonales)

cedula = input("Ingrese su cédula: ")
print("cédula:", cedula)
nombre = input("Ingrese su nombre: ")
print("nombre:", nombre)
correo = input("Ingrese su correo: ")
print("correo:", correo)
datospersonales.append(cedula)
datospersonales.append(nombre)
datospersonales.append(correo)
print(datospersonales)



