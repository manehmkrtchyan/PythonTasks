from user import User 
from product import Product
from shopping_cart import ShoppingCart


pr = Product('sexan', 30000, 1234, {'material': 'wood', 'color': 'black'})
pr2 = Product('sexan', 70000, 12345, {'material': 'wood', 'color': 'black'})
sc = ShoppingCart(pr.get_id())
#print(pr)
(sc.add_to_cart(pr))
(sc.add_to_cart(pr2))
print(sc.product_list)
print(sc.total_price())