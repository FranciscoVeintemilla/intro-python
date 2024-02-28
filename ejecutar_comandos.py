import os
import platform

print(platform.system())
print(platform.release())
comando = input('ingrese el comando a ejecutar: ')
rt = None
try:
    rt = os.system(comando)
except Exception as e:
    print(e)
if rt == 0:
    print('La ejecucion fue correcta')
else:
    print('La ejecucion no fue correcta')