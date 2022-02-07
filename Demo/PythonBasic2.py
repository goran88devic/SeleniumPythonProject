if 5 > 3:
    print("5 is greater then 3")


num = 1
if num > 0:
    print("This is positive num")
elif num == 0:       #====="else if" in javascript
    print("Num is 0")
else:
    print("This is negative number")


num = [1,2,3,4,5]
for val in num:
    print(val)

num = [1,2,3,4,5]
sum=0
for val in num:
    sum=sum+val
    print("Total for every single row is ", sum)

num = [1,2,3,4,5]
sum=5
for val in num:
    sum=sum+val
print("Total is ", sum)


fruits = ["apple","oranges","grapes"]
for val in fruits:
    print(val)
else:
    print("no fruits left")



print("Enter a number: ")
num = int(input()) #we must convert string in int type
sum = 0
i = 1

while i<num:
    sum=sum+i
    i=i+1
print("Total is :", sum)




