# Estoque do Restaurante

# Dicionário para armazenar os produtos e suas quantidades
estoque = {}

def adicionar_produto(nome, quantidade):
    """Adiciona um produto ao estoque"""
    if nome in estoque:
        estoque[nome] += quantidade
    else:
        estoque[nome] = quantidade
    print(f"Produto '{nome}' adicionado ao estoque com {quantidade} unidades.")

def remover_produto(nome, quantidade):
    """Remove um produto do estoque"""
    if nome in estoque:
        if estoque[nome] >= quantidade:
            estoque[nome] -= quantidade
            print(f"Produto '{nome}' removido do estoque com {quantidade} unidades.")
        else:
            print(f"Não há suficientes unidades de '{nome}' no estoque.")
    else:
        print(f"Produto '{nome}' não encontrado no estoque.")

def consultar_estoque():
    """Exibe o estoque atual"""
    print("Estoque atual:")
    for produto, quantidade in estoque.items():
        print(f"  {produto}: {quantidade} unidades")

def main():
    while True:
        print("Menu:")
        print("  1. Adicionar produto ao estoque")
        print("  2. Remover produto do estoque")
        print("  3. Consultar estoque")
        print("  4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade: "))
            adicionar_produto(nome, quantidade)
        elif opcao == "2":
            nome = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade: "))
            remover_produto(nome, quantidade)
        elif opcao == "3":
            consultar_estoque()
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()