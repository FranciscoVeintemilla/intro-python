import paramiko # Para establecer conexiones SSH
import sys # Para accder a los argumentos en linea de comandos
import os # Para interactuar con el sistema operativo
from datetime import datetime # Para manejar fecha y hora


def scan_ports(ip): # Definir una funcion que escanea los puertos de una ip
    """
    Como escanear puerto de direcciones IP

    Args:
        ip (str): IP a escanear.
    """
    ports_to_scan = [21, 22, 80, 443]  # Puertos para escanear (FTP, SSH, HTTP y HTTPS)
    open_ports_found = False # Variable para indicar si hay puertos abiertos

    for port in ports_to_scan:
        try:
            # Crear un objeto cliente SHH
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(ip, port=port, timeout=5) # 5 Seg tiempo limite para la conexion
            client.close()
            open_ports_found = True  # Se encontró al menos un puerto abierto
            print(f"El puerto {port} está abierto en {ip}") # Este es el mensaje que presenta hay algun puerto abierto
        except (paramiko.AuthenticationException, paramiko.SSHException, OSError, TimeoutError) as e:
            # Manejo de errores específicos
            # Imprimir un mensaje indicando la novedad al escanear el puerto
            print(f"Novedad al escanear en puerto {port}: {e}")

    if open_ports_found:
        print(f"La siguiente ip tiene puertos abiertos {ip}") # Solo si se logra la conexion
    else:
        print(f"No se encontraron puertos abiertos en la ip {ip}") # Cuando no hay puerto abiertos o no se logro conectar

    # Imprimir la fecha y hora actual
    print("Fecha y hora de escaneo:", datetime.now())

def print_system_info():
    """
    Información del sistema operativo en el que se ejecuta
    """
    print("Info PC Francisco principal")
    print(f"Sistema operativo: {os.name}")
    if os.name == 'nt':
        print(f"Nombre del sistema: {os.environ['COMPUTERNAME']}")
        print(f"Versión del sistema: {os.environ['OS']}")
    else:
        print(f"Nombre del sistema: {os.uname().sysname}")
        print(f"Versión del sistema: {os.uname().release}")
        print(f"Procesador: {os.uname().machine}")

#Definir la funcion principal de la herramienta
def main():
    if len(sys.argv) != 2:
        print("Uso: python NuevoProyecto.py <dirección_ip>")
        sys.exit(1)

    ip = sys.argv[1] # Asigna el primer argumento (ip)
    scan_ports(ip) # Escanea los puertos (ip)
    print_system_info() #Imprime la informacion del sistema

if __name__ == "__main__":
    main()

