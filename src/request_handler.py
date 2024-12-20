class RequestHandler:
    def __init__(self, inventory_manager):
        self.inventory_manager = inventory_manager

    def register_request(self, product_name, sector, quantity):
        if self.inventory_manager.process_request(product_name, quantity):
            print(f"Solicitação registrada: {quantity} de '{product_name}' para o setor '{sector}'.")
        else:
            print(f"Estoque insuficiente para o produto '{product_name}'.")