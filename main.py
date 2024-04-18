from binary_search_tree import BinarySearchTree
import os

absFilePath = os.path.abspath(__file__)
path, filename = os.path.split(absFilePath)
path2 = path + "\\texts\\text"

def read_files(file: str, binary_tree: BinarySearchTree[str], i: int):
    try:
        with open(file) as archivo:
            sentences = archivo.read()

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
        read_files(path2 + str(i + 1) + '.txt', binary_tree, i+1)

    print('--BUSCADOR DE PALABRAS--')
    ref_word = input('Ingrese la palabra para buscar: ')
    resultado = binary_tree.search(ref_word)
    if resultado is None:
        print('No existe esta palabra en los archivos.')
    else:
        print(f'Palabra buscada: {resultado["word"]}\n'
              f'Aparece en los archivos: {resultado["reference"]}')



    return 0


main()
