print("Hello World..")

# ------------variables--------------
x = 5
y = "Automation"
print(x)
print(y)

#----------syntax-----------
print("Hello" + y)

x = 10
y = 20
print(x+y)

if 10 > 5:
    print("10 is greater than 5")
#----------function--------------
def sum(a,b):
    print(a+b)

x = sum(25,35)


#--------numbers--------------------
x = 5
y = 2.5
z = 4j

print(type(x))
print(type(y))
print(type(z))

x = int(2)
y = int(2.5)
z = float(1)
p = str(10)

print(x)
print(y)
print(z)
print(p)

#--------strings-----------
x = " Hello World.."
print(x)
print(x[1])
print(x[6:11])
print(len(x))
print(x.lower())
print(x.upper())
print(x.strip())
print(x.replace("e","a"))
print(x.split(","))


#----------input---------
print("enter your name")
x = input()
print("Hello" + x)


