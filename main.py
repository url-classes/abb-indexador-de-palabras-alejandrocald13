from binary_search_tree import BinarySearchTree
import os

absFilePath = os.path.abspath(__file__)
path, filename = os.path.split(absFilePath)
path2 = path + "\\texts\\text"


def read_files(file: str, binary_tree: BinarySearchTree[str], i: int):
    try:
        with open(file) as archivo:
            sentences = archivo.read()  # se leen todos los archivos :)

    except FileNotFoundError:
        print('El archivo no existe.')

    new_word = ''
    for word in sentences:
        if word == ' ' or word == '.':
            if i != -3:

                diccionario = {'word': new_word.lower(), 'reference': [i]}
                binary_tree.insert(diccionario)

            else:
                pass

            new_word = ''

        else:
            new_word += word


def main():
    binary_tree = BinarySearchTree()
    for i in range(10):
        read_files(path2 + str(i + 1) + '.txt', binary_tree, i+1)   # lee cada uno de los archivos automaticamente

    print('--BUSCADOR DE PALABRAS--')
    ref_word = input('Ingrese la palabra para buscar: ')  # pide que palabra quiere
    resultado = binary_tree.search(ref_word)
    if resultado is None:
        print('No existe esta palabra en los archivos.')  # si se obtiene nada, solo imprime nada
    else:
        print(f'Palabra buscada: {resultado["word"]}')  # si encuentra algo, entonces imprime al palabra

        i = 0
        j = 1  # se crean dos contadores, que indican en que posición y cuantas veces aparece

        if len(resultado["reference"]) == 1:  # se hace una excepción si es unico!
            print(f'Aparece en el Archivo No.{resultado["reference"][0]} -> 1 vez.')
        else:

            while True:

                i += 1  # se pasa a la siguiente posición

                if i == len(resultado["reference"]):  # acá es para determinar cuando ya llegó a la última casilla
                    print(f'Aparece en el Archivo No.{resultado["reference"][i-1]} -> {j} veces.')
                    break

                if resultado["reference"][i-1] == resultado["reference"][i]:  # compara el valor anterior con el actual
                    j += 1  # se va sumando cuantas veces aparece
                else:
                    w = resultado["reference"][i-1]  # se toma cual es el numero de archivo actual
                    print(f'Aparece en el Archivo No.{w} -> {j} veces.')  # se imprimen ambas varibales
                    j = 1  # se reinicia el contador para saber cuantas hay actualmente es decir uno

    return 0


main()  # se llama a main
