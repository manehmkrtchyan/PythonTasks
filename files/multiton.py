class Multiton:
    count = 3
    ls = []
    counter = -1

    def __new__(cls):
        if len(cls.ls) < cls.count:
            cls.ls.append(super().__new__(cls))
        cls.counter += 1
        return cls.ls[cls.counter % cls.count]
    
    @classmethod
    def change_count(cls, new_count):
        cls.count = new_count
