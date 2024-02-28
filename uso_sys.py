import os

print(os.sep)
print(os.getcwd())
print(os.chdir("C:\\Users\\USER\\PycharmProjects\\POO BASICO\\"))
print(os.getcwd())
print(os.listdir())
print('---------------')
print(os.getcwd())
print('Los elemntos de la siguiente ruta son:')
for nombre in os.listdir():
    print(f'{nombre}')
print('-----------------')
print(os.listdir("C:\\Users\\USER\\PycharmProjects"))
os.chdir("C:\\Users\\USER\\PycharmProjects")
try:
    os.mkdir("test1")
except Exception as e:
    print('No se pude crear el directorio porque ya existe', e)
print(os.listdir())
os.chdir("C:\\Users\\USER\\PycharmProjects\\test1\\")
#os.makedirs('xx\\yy')
print('-'.center(50,'-'))
print(os.environ)
print(os.getpid())


