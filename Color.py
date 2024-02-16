def obtener_color():
    numero = int(input("Ingresa un número: "))
    if numero == 1:
        return 'ese es Azul'
    elif numero == 2:
        return 'ese es Rojo'
    elif numero == 3:
        return 'ese es Verde'
    else:
        return 'El número no pertenece a ninguna rango'

def main():
    color = obtener_color()
    print(color)

if __name__ == "__main__":
    main()
