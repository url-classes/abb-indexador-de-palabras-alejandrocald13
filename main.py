from binary_search_tree import BinarySearchTree


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
                print(diccionario)
                binary_tree.insert(diccionario)

            else:
                pass

            new_word = ''

        else:
            new_word += word


def main():
    binary_tree = BinarySearchTree()
    for i in range(2):
        read_files(input('Ingresa la dirección del archivo: '), binary_tree, i+1)

    print(binary_tree.preorder())

    return 0


main()
