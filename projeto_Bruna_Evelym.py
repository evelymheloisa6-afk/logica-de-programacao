 [
    {
        "codigo": 101,
        "titulo": "Titanic",
        "genero": "Romance",
        "ano": 1997,
        "nota": 9.5
    },
    {
        "codigo": 102,
        "titulo": "Velozes e Furiosos",
        "genero": "Acao",
        "ano": 2001,
        "nota": 8.5
    },
    {
        "codigo": 103,
        "titulo": "Invocacao do Mal",
        "genero": "Terror",
        "ano": 2013,
        "nota": 9.0
    }
]

def exibir_menu():
    print("\n========== SISTEMA DE FILMES ==========")
    print("1 - Cadastrar filme")
    print("2 - Listar filmes")
    print("3 - Buscar filme")
    print("4 - Remover filme")
    print("5 - Sair")
    print("=======================================")

def buscar_indice(lista, pesquisa):
    for indice in range(len(lista)):
        filme = lista[indice]

        if str(filme["codigo"]) == pesquisa:
            return indice

        if filme["titulo"].lower() == pesquisa.lower():
            return indice

    return -1

def cadastrar(lista):
    try:
        print("\n--- CADASTRAR FILME ---")

        codigo = int(input("Digite o codigo do filme: "))

        if buscar_indice(lista, str(codigo)) != -1:
            print("Esse codigo ja esta cadastrado!")
            return

        titulo = input("Digite o titulo: ").strip()
        genero = input("Digite o genero: ").strip()

        if titulo == "" or genero == "":
            print("O titulo e o genero nao podem ficar vazios.")
            return

        ano = int(input("Digite o ano de lancamento: "))
        nota = float(input("Digite a nota do filme (0 a 10): "))

        if ano < 1888 or ano > 2026:
            print("Ano invalido. Digite um ano entre 1888 e 2026.")
            return

        if nota < 0 or nota > 10:
            print("Nota invalida. Digite um valor entre 0 e 10.")
            return

        novo_filme = {
            "codigo": codigo,
            "titulo": titulo,
            "genero": genero,
            "ano": ano,
            "nota": nota
        }

        lista.append(novo_filme)
        print("Filme cadastrado com sucesso!")

    except ValueError:
        print("Entrada invalida. Confira os campos numericos.")

def listar(lista):
    print("\n--- LISTA DE FILMES ---")

    if len(lista) == 0:
        print("Nenhum filme cadastrado.")
        return

    for filme in lista:
        print("----------------------------------------")
        print("Codigo:", filme["codigo"])
        print("Titulo:", filme["titulo"])
        print("Genero:", filme["genero"])
        print("Ano:", filme["ano"])
        print("Nota:", filme["nota"])

    print("----------------------------------------")


def buscar(lista):
    print("\n--- BUSCAR FILME ---")

    pesquisa = input("Digite o codigo ou o titulo do filme: ").strip()

    if pesquisa == "":
        print("Digite uma informacao para realizar a busca.")
        return

    indice = buscar_indice(lista, pesquisa)

    if indice != -1:
        filme = lista[indice]

        print("\nFilme encontrado!")
        print("Codigo:", filme["codigo"])
        print("Titulo:", filme["titulo"])
        print("Genero:", filme["genero"])
        print("Ano:", filme["ano"])
        print("Nota:", filme["nota"])

    else:
        print("Filme nao encontrado.")


# Funcao para remover um filme
def remover(lista):
    print("\n--- REMOVER FILME ---")

    pesquisa = input(
        "Digite o codigo ou o titulo do filme que deseja remover: "
    ).strip()

    if pesquisa == "":
        print("Digite uma informacao para realizar a busca.")
        return

    indice = buscar_indice(lista, pesquisa)

    if indice != -1:
        removido = lista.pop(indice)
        print("Filme removido:", removido["titulo"])

    else:
        print("Nao foi possivel remover: filme nao encontrado.")


# Funcao principal do programa
def principal():
    while True:
        exibir_menu()

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar(filmes)

        elif opcao == "2":
            listar(filmes)

        elif opcao == "3":
            buscar(filmes)

        elif opcao == "4":
            remover(filmes)

        elif opcao == "5":
            print("Sistema encerrado. Ate mais!")
            break

        else:
            print("Opcao invalida. Escolha de 1 a 5.")


# Inicia o programa
principal()
