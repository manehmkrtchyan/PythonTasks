class Product:
    def __init__(self, name, price, id, description: 'dict'):
        self._name = name
        self._price = price
        self._id = id
        self._description = description

    def get_name(self):
        return self._name
    def set_name(self, new_name):
        self._name = new_name
    
    def get_price(self):
        return self._price
    
    def set_price(self, new_price):
        self._price = new_price
    
    def get_id(self):
        return self._id
    
    def get_description(self):
        return self._description
    
    def set_description(self, new_description: 'dict'):
        self._description = new_description
    
    def __repr__(self):
        return str(dict(name=self._name, price=self._price, id=self._id, description=self._description))
    