def printHello():
    print("Hello")

printHello()

def printHi(name="John"):
    print("Hi,"+ name)

printHi("Goran")
printHi()


def sum(a,b,c):
    print(a+b+c)
sum(20,30,40)

def returnSum(a,b):
    return (a+b)

x = returnSum(10,20)
print(x)
