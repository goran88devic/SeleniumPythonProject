my_set = {"Chalk", "Duster", "Board"}
print(my_set)

for x in  my_set:
    print(x)

print("Chalk" in my_set)

my_set.add("Pen")
print(my_set)

my_set.update(["Pencil", "Eraser"])
print(my_set)

my_set.remove("Pencil")
print(my_set)

my_set.discard("Pen") #use 'discard' command if you not sure is element exist
print(my_set)

my_set.pop()
print(my_set)

my_set.clear()
print(my_set)

del my_set

my_list = [1,2,3]
print(my_list)
my_set_3 = set(my_list)
print(my_set_3)

# UNION | INTERSECTION | DIFF | SYMMETRIC DIFF




