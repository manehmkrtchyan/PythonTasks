class Obj:
    def __init__(self) -> None:
        self.stack = []
        self.history = []
        
    def write(self, string):
        self.stack.append(string)
        
    def undo(self):
        a = self.stack.pop()
        self.history.append(a)
        
    def redo(self):
        self.stack.append(self.history[-1])
        self.history.pop()
        
    def show(self):
        print(self.stack)
        
obj = Obj()
obj.write('Barev')
obj.write('Dzez')
obj.write('Vonc')
obj.show()
obj.undo()
obj.undo()
obj.show()
obj.redo()
obj.show()
