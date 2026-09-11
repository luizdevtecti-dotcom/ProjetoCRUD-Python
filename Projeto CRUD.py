import os

def limpar_tela():
    os.system('cls')

def pausar():
    input("Pressione ENTER para continuar...")

def menuPrincipal(): #MENU PRINCIPAL
    limpar_tela()
    print("=================================")
    print("=== CADASTRO DE JOGOS ZERADOS ===")
    print("======== 0 - SAIR ===============")
    print("======== 1 - ADICIONAR ==========")
    print("======== 2 - LISTAR =============")
    print("======== 3 - ATUALIZAR ==========")
    print("======== 4 - REMOVER ============")
    print("======== 5 - BUSCAR =============")
    print("= Desenvolvido por: Luiz Miguel =")
    print("========= Versão:3.0 ============")
    print("=================================")

def adicionarJogos(lista):  # ADICIONAR
    continuar = "s"
    while continuar == "s":
        limpar_tela()
        print("=================================")
        print("======== Adicionar Jogo =========")
        print("=================================")
        nomeJogo = input("Digite o nome do jogo zerado: ").strip()
        
        if nomeJogo != "":
            lista.append(nomeJogo)
            print("Jogo cadastrado com sucesso!")
        else:
            print("O nome do jogo não pode ser vazio!")

        continuar = input("Deseja cadastrar outro jogo? (S/N): ").lower()
        while continuar != "n" and continuar != "s":
            print("Opção inválida! Apenas S/N")
            continuar = input("Deseja cadastrar outro jogo? (S/N): ").lower()

def listarJogos(lista):  # LISTAR
    limpar_tela()
    print("=================================")
    print("==== Lista de jogos zerados =====")
    print("=================================")
    if len(lista) == 0:
        print("A lista está vazia!")
    else:
        for i in range(len(lista)):
            print(f"ID: {i + 1} | Jogo: {lista[i]}")
    pausar()

def atualizarJogos(lista):  # ATUALIZAR
    limpar_tela()
    print("=================================")
    print("======= Atualizar jogos =========")
    print("=================================")
    if len(lista) == 0:
        print("A lista está vazia!")
        pausar()
    else:
        for i in range(len(lista)):
            print(f"ID: {i + 1} | Jogo: {lista[i]}")

        try:
            idJogo = int(input("Digite o ID que deseja atualizar: "))
            indiceA = idJogo - 1

            if indiceA >= 0 and indiceA < len(lista):
                confirmar = input(f"Tem certeza que deseja atualizar o jogo '{lista[indiceA]}'? (s/n): ").lower()
                if confirmar == 's':
                    novoNome = input(f"Digite o novo nome para {lista[indiceA]}: ").strip()
                    if novoNome != "":
                        lista[indiceA] = novoNome
                        print("Jogo foi atualizado com sucesso!")
                    else:
                        print("O nome não pode ser vazio!")
                else:
                    print("Atualização cancelada!")
                pausar()
            else:
                print("O ID está inválido")
                pausar()
        except ValueError:
            print("O ID precisa ser um número!")
            pausar()

def removerJogo(lista):  # REMOVER
    limpar_tela()
    print("==================================")
    print("======== Remover jogos ===========")
    print("==================================")
    if len(lista) == 0:
        print("A lista está vazia!")
        pausar()
    else:
        print("==== Lista de jogos zerados =====")
        for i in range(len(lista)):
            print(f"ID: {i + 1} | Jogo: {lista[i]}")

        try:
            idRemover = int(input("Digite o ID que deseja remover: "))
            indiceR = idRemover - 1

            if indiceR >= 0 and indiceR < len(lista):
                confirmaRemover = input(f"Tem certeza que deseja remover o jogo '{lista[indiceR]}'? (s/n): ").lower()
                if confirmaRemover == 's':
                    lista.pop(indiceR)
                    print("Jogo foi removido com sucesso!")
                else:
                    print("Remoção cancelada!")
                pausar()
            else:
                print("O ID está inválido")
                pausar()
        except ValueError:
            print("O ID precisa ser um número!")
            pausar()

def buscarJogo(lista):  # BUSCAR
    limpar_tela()
    print("=================================")
    print("======== Buscar jogos ===========")
    print("=================================")
    if len(lista) == 0:
        print("A lista está vazia!")
        pausar()
    else:
        nome = input("Digite o nome do jogo que deseja buscar: ").strip()

        encontrado = False
        indJogo = None
        for indice in range(len(lista)):
            if nome.lower() == lista[indice].lower():
                indJogo = indice
                encontrado = True

        if encontrado:
            print(f"O jogo ID: {indJogo + 1} - {lista[indJogo]} foi encontrado")
        else:
            print(f"O jogo '{nome}' não foi encontrado")
        pausar()

listaJogos = []
continuar = 's'

while continuar.lower() == 's':
    menuPrincipal()
    opcao = input("Digite uma opção: ")

    match opcao:
        case '1':
            adicionarJogos(listaJogos)

        case '2':
            listarJogos(listaJogos)

        case '3':
            atualizarJogos(listaJogos)

        case '4':
            removerJogo(listaJogos)

        case '5':
            buscarJogo(listaJogos)

        case '0':
            confirmar = input("Deseja realmente sair? (s/n): ").lower()
            if confirmar == 's':
                print("\nObrigado por usar o sistema de jogos zerados!")
                print(" Desenvolvido por: Luiz Miguel ")
                print("======== Versão: 3.0 ===========")
                continuar = 'n'
            else:
                print("Saída cancelada!")
                pausar()
        case _:
            print("\nOpção inválida!")
            pausar()