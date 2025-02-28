# 1. Crie um programa em Python que permita ao usuário cadastrar produtos em estoque. 
# Cada produto será armazenado como uma lista contendo o nome do produto, o preço e a quantidade em estoque. 
# O programa deve permitir adicionar novos produtos, exibir todos os produtos cadastrados, 
# buscar um produto pelo nome e calcular o valor total em estoque de um produto específico (preço * quantidade).

# NÃO É PERMITIDO O USO DE FUNÇÃO OU QUALQUER ESTRUTURA QUE NÃO FOI APRESENTADA NA AULA!
print('Bem-vindo ao sistema de estoque, Escolha a operação:')

lista_produtos = [{'Produto': 'Arroz', 'Preço': 10.0, 'Quantidade': 100},
                    {'Produto': 'Feijão', 'Preço': 8.0, 'Quantidade': 50},
                    {'Produto': 'Macarrão', 'Preço': 5.0, 'Quantidade': 80}]

while True:
    print('\nEscolha uma operação ou digite *fim* para sair:')
    operacao = input('1 - Adicionar produto\n2 - Exibir produtos\n3 - Buscar produto\n4 - Calcular valor total\n')



    if operacao == '1':
        produto = input('Digite o nome do produto: \n')
        preco = float(input('Digite o preço do produto: \n'))
        quantidade = int(input('Digite a quantidade em estoque: \n'))
        lista_produtos.append({'Produto': produto, 'Preço': preco, 'Quantidade': quantidade})
        print("Produto Adicionado!")

        for produto in lista_produtos:
            print(produto)

    elif operacao == '2':
        print("Lista de Produtos no Estoque: \n")
        for produto in lista_produtos:
            print(produto) 

    elif operacao == '3':
        nome_produto = input("Digite o produto que deseja buscar: \n")
        produto_busca = False
        for produto in lista_produtos:
            if produto['Produto'] == nome_produto:
                print(produto)
                produto_busca = True
                break
        if produto_busca == False:
                    print("\nEste não foi encontrado no Estoque")

    elif operacao == '4': 
        nome_produto = input("Digite o produto para calcular o valor total: \n")
        produto_busca = False
        for produto in lista_produtos:
            if produto['Produto'] == nome_produto:
                valor = produto['Preço'] * produto['Quantidade']
                print(f"O valor total do produto {nome_produto} é: {valor}")
                produto_busca = True
                break
        if produto_busca == False:
                    print("\nEste produto não está cadastrado no Estoque")
           

    elif operacao == 'fim':
        break;



