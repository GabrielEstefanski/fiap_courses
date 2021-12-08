def perguntar():
    perguntas = input("O que deseja realizar?\n" +
                "<I> - Inserir um usuário: \n" +
                "<P> - Pesquisar um usuário: \n" +
                "<E> - Excluir um usuário: \n" +
                "<L> - Listar usuários: \n" 
    ).upper()

    return (perguntas)

def inserir(dicionario):
    dicionario[input("Digite o Login: ")] = [input("Digite o nome: ").upper(),
                                              input("Digite a data: "), 
                                              input("Digite o setor: ").upper()]


