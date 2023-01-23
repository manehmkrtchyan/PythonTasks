class ShoppingCart:
    def __init__(self, user_id):
        self.id = user_id
        self.product_list = []
    
    def add_to_cart(self, product):
        self.product_list.append(product)
    
    def remove_from_cart(self, product):
        self.product_list.remove(product)
    
    def total_price(self):
        total_price = 0
        for product in self.product_list:
            total_price += product.get_price()
        return total_price
