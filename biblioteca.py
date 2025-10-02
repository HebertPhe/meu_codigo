# Sistema de Biblioteca, todos os passo a passo a seguir:

# 1: Fazer import do que precisa e fazer as funções pra cada opção

import uuid

livros = {}
usuarios = {}

# Adicionar Livro
def adicionar_livro():
    titulo = input("Título do livro: ")
    autor = input("Autor do livro: ")
    id_livro = str(uuid.uuid4())[:8]  # ID único simples
    livros[id_livro] = {
        'titulo': titulo,
        'autor': autor,
        'disponivel': True
    }
    print(f"Livro '{titulo}' adicionado com ID {id_livro}.\n")


# Remover Livro
def remover_livro():
    listar_todos_livros()
    id_livro = input("Digite o ID do livro a ser removido: ")
    if id_livro in livros:
        del livros[id_livro]
        print("Livro removido com sucesso.\n")
    else:
        print("ID não encontrado.\n")


# Listar todos os livros da biblioteca
def listar_todos_livros():
    print("\n--- Lista de todos os livros ---")
    if not livros:
        print("Nenhum livro na biblioteca.\n")
    for id_livro, dados in livros.items():
        status = "Disponível" if dados['disponivel'] else "Emprestado"
        print(f"[{id_livro}] {dados['titulo']} - {dados['autor']} ({status})")
    print()


# Registrar usuários
def registrar_usuario():
    nome = input("Nome do usuário: ")
    id_usuario = str(uuid.uuid4())[:8]
    usuarios[id_usuario] = {
        'nome': nome,
        'emprestimos': []
    }
    print(f"Usuário '{nome}' registrado com ID {id_usuario}.\n")


# Registrar empréstimo de livros
def registrar_emprestimo():
    listar_todos_livros()
    id_livro = input("ID do livro a ser emprestado: ")
    if id_livro not in livros or not livros[id_livro]['disponivel']:
        print("Livro não disponível para empréstimo.\n")
        return
    listar_usuarios()
    id_usuario = input("ID do usuário: ")
    if id_usuario not in usuarios:
        print("Usuário não encontrado.\n")
        return
    livros[id_livro]['disponivel'] = False
    usuarios[id_usuario]['emprestimos'].append(id_livro)
    print(f"Livro emprestado para {usuarios[id_usuario]['nome']}.\n")


# Listar usuários da biblioteca
def listar_usuarios():
    print("\n--- Lista de usuários ---")
    if not usuarios:
        print("Nenhum usuário registrado.\n")
    for id_usuario, dados in usuarios.items():
        print(f"[{id_usuario}] {dados['nome']}")
    print()


# Consultar livros disponíveis e emprestados
def consultar_disponiveis_emprestados():
    print("\n--- Livros Disponíveis ---")
    for id_livro, dados in livros.items():
        if dados['disponivel']:
            print(f"[{id_livro}] {dados['titulo']} - {dados['autor']}")
    print("\n--- Livros Emprestados ---")
    for id_livro, dados in livros.items():
        if not dados['disponivel']:
            print(f"[{id_livro}] {dados['titulo']} - {dados['autor']}")
    print()


# 2: Criação do menu em laço de repetição
#def menu():
#    while True:
#        print("=== Sistema de Biblioteca ===")
#        print("1. Adicionar livros à biblioteca.")
#        print("2. Remover livros da biblioteca.")
#        print("3. Listar todos os livros disponíveis.")
#        print("4. Registrar usuários.")
#        print("5. Registrar empréstimos de livros.")
#        print("6. Consultar livros emprestados e disponíveis.")
#        print("0. Sair")
#        escolha = input("Escolha uma opção: ")

<<<<<<< HEAD
#        if escolha == '1':
#            adicionar_livro()
#        elif escolha == '2':
#            remover_livro()
#        elif escolha == '3':
#            listar_todos_livros()
#        elif escolha == '4':
#            registrar_usuario()
#        elif escolha == '5':
#            registrar_emprestimo()
#        elif escolha == '6':
#            consultar_disponiveis_emprestados()
#        elif escolha == '0':
#            print("Saindo do sistema...")
#            break
#        else:
#            print("Opção inválida. Tente novamente.\n")

# 3: Função para iniciar sistema da biblioteca
#if __name__ == '__main__':
    menu()
=======
        if escolha == '1':
            adicionar_livro()
        elif escolha == '2':
            remover_livro()
        elif escolha == '3':
            listar_todos_livros()
        elif escolha == '4':
            registrar_usuario()
        elif escolha == '5':
            registrar_emprestimo()
        elif escolha == '6':
            consultar_disponiveis_emprestados()
        elif escolha == '0':
            print("Saindo do sistema... Obrigado pelo serviço!")
            break
        else:
            print("Opção Inválida. Tente novamente.\n")

# 3: Função para iniciar sistema da biblioteca
if __name__ == '__main__':
    menu()

# Menu com laço de repetição feito
# Anotação pra fazer um segundo commit e salvar ele com o menu funcionando além das funções
>>>>>>> f1acee7 (Segunda commit com o menu no código)
