from func import *
usuarios = {}
opcao = perguntar()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)

    elif opcao == "P":
        login = input("Digite o login: ")
        print(usuarios.get(login))

    elif opcao == "E":
        login = input("Digite o login: ")
        del usuarios[login]
        print("Usuário do login: " + login + " excluído")

    elif opcao == "L":
        print(usuarios)

    opcao = perguntar()

print ("\nFinalizando o código")