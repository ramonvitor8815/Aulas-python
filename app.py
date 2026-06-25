categorias = (  
    "Eletronicos",
    "Alimentos",
    "Roupas"
)
estoque = []

while True:

    print("SISTEMA DE ESTOQUE")

    print("1 - Cadastro de Produto")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        nome = input("Digite o nome do Produto: ")

        for i in range(len(categorias)):
            print(i + 1, "-", categorias[i])

        escolha = int(input("Ecolha a categoria: "))

        preco = float(input("Preço:"))

        quantidade = int(input("Quantidade: "))

        produto = {
            "nome": nome, 
            "categoria": categorias[escolha - 1],
            "preço":preco,
            "quantidade":quantidade
        }

        estoque.append(produto)
    
    elif opcao == "5":
        break
    else:
        print("opção invalida")