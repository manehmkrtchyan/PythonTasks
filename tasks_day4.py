'1'
n = int(input("Enter the the length of the list: "))

self = []
for i in range(1, n + 1):
    self.append(i)

target  = []
ele = input("Enter the target list: ")
while ele != "":
    target.append(ele)
    ele = input("Enter the target list: ")
target = [int(ele) for ele in target]

def build(self, target):
    output=[]
    for i in self:
        if i in target:
            output.append("Push")
        elif(i<=max(target)):
            output.append("Push")
            output.append("Pop")
        else:
            break
    return output
print(build(self, target))