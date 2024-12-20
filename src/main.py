from inventory_manager import InventoryManager
from request_handler import RequestHandler

def main():
    excel_file = 'src/estoque.xlsx'  # Certifique-se de que o caminho está correto
    inventory_manager = InventoryManager(excel_file)
    request_handler = RequestHandler(inventory_manager)

    while True:
        print("\n1. Adicionar Produto")
        print("2. Registrar Solicitação")
        print("3. Exibir Estoque")
        print("4. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            product_name = input("Nome do Produto: ")
            quantity = int(input("Quantidade: "))
            inventory_manager.add_product(product_name, quantity)
        elif choice == '2':
            product_name = input("Nome do Produto: ")
            sector = input("Setor: ")
            quantity = int(input("Quantidade: "))
            request_handler.register_request(product_name, sector, quantity)
        elif choice == '3':
            inventory = inventory_manager.display_inventory()
            for product, qty in inventory.items():
                print(f"{product}: {qty}")
        elif choice == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()