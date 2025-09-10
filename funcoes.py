# funcoes.py
def exibir_menu():
    print("\n[1] cadastrar item [2] listar intens [0] sair")

    def cadastrar_item(itens):
        nome = input("estudo dirigido:").strip()
        if not nome:
            print("estudo dirigido")
            print("item ja existe:")
            itens.append(nome)
            print("item cadastrado!")

            def listar(itens):
             if not itens:
                print("Nenhum iten cadastardo.")

        else:
              for i, nome in enumerate(itens,start=1):
               print(f"{i}. {nome}")

