from datetime import datetime

current_time = datetime.now().strftime("%H:%M:%S")

class Gortik:
    def __init__(self, ) -> None:
        self.state = "alive"
    
    def wake_up(self):
        if sun.is_shining():
            return("Hi! My name is Gortik. Welcome to my world!")
        return ("Let me sleep!!")
    
    def sleep(self):
        if sun.is_shining:
            return "I don't want to sleep."
        return("It's bedtime. Bye!")
    
    def breathe(self):
        if tree.oxygen:
            return ("Now I'm breathing.")
        return "I don't breathe while I'm sleeping."
    def eat(self, count):
        if flowers.count >= count:
            flowers.count -= count 
            return(f"I ate {count} flowers. There are {flowers.count} flowers yet to eat. ")
        elif flowers.count == 0:
            gortik.state = "dead"
            return f"I have nothing to eat I am dying. Check the code to save me!"
        else:
            return "There aren't enough flowers for me to eat. Decrease the count."

class Flowers():
    def __init__(self):
        self.count = 100
       
class Sun:
    def __init__(self) -> None:
        pass
    def is_shining(self):
        if int(current_time[:2]) >= 12: #Sun shines since 12:00 AM till 23:59 PM in Gortik's world.
            return True
        return False

class Tree:
    def __init__(self) -> None:
        pass
    def oxygen(self):
        if sun.is_shining():
            return True


flowers = Flowers()
sun = Sun()
tree = Tree()  
gortik = Gortik()



print(gortik.wake_up())
print(gortik.eat(5))
print(gortik.breathe())
print(gortik.eat(93))
print(gortik.eat(3))
print(gortik.eat(2))
print(gortik.eat(4))
print(gortik.sleep())