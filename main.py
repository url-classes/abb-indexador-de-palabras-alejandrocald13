def read_files(file: str) -> str:

    try:
        with open(file) as archivo:
            return archivo.read()

    except FileNotFoundError:
        print('El archivo no existe.')


def main():
    print(read_files(input('Ingresa la dirección del archivo: ')))

    return 0


main()