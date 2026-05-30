class OrderMenu:
    def __init__(self):
        self.menu_list = [
            {"name": "Espresso", "price": 15000},
            {"name": "Latte", "price": 20000},
            {"name": "Cappuccino", "price": 18000}
        ]
        self.selected_order = None

    def select(self, index):
        if 0 <= index < len(self.menu_list):
            self.selected_order = self.menu_list[index]

    def get_order(self):
        return self.selected_order