
def cadastrar(lista, item):
    lista.append(item)
    print("item cadastrado!")

    def listar(lista):
        if not lista:
            print("A lista está vazia.")
        else:
            for i, item in enumerate(lista, 1):
                print(f"{i}. {item}")
