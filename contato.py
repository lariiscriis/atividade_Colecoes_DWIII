# 2. Crie um programa em Python que permita ao usuário cadastrar seus contatos com nome e número de telefone. 
# O programa deve utilizar um dicionário para armazenar os contatos, onde o nome é a chave e o número de telefone é o valor. 
# O programa deve permitir adicionar novos contatos, exibir todos os contatos cadastrados e buscar um contato pelo nome.


print('Bem-vindo a sua agenda, Escolha a operação:')

agenda = {'João': '1111-1111', 'Maria': '2222-2222', 'José': '3333-3333'}

while True:
        operacao = input("1 - Adicionar contato\n2 - Exibir lista de contatos\n3 - Buscar contato\n")

        if operacao == '1':
            nome = input("Digite o nome do contato: \n")
            telefone = input("Digite o número do contato: \n")

            agenda[nome] = telefone

            print("\nContato Adicionado!")
            print(agenda)

        elif operacao == '2':
            print("\nLista de Contatos: \n")
            for nome,contato in agenda.items(): 
                print(f"Nome: {nome} | Contato: {contato}")

        elif operacao == '3':
            nome_busca = input("Digite o nome do contato que deseja buscar: \n")
            contato_bool = False
            for nome,contato in agenda.items(): 
                if nome == nome_busca: 
                    print(f"Nome: {nome} | Contato: {contato}")
                    contato_bool = True 
                    break
            if contato_bool == False:
                print("\nEste contanto não existe na lista de contantos")

        elif operacao == 'fim':
            break;