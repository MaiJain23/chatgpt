print(1)
print(2)
print(3)
print(4)
print(5)

# 1 to 100
#for loop 
for x in range(1,101):
    print(x)

#program 2

for x in range(5):
    print(x)

#program 3
for x in range(1,4):
    print('hello')
    print('bye')

#program 4
for x in range(2,21,2):
    print(x)

#print(5,1)
for x in range(5,0,-1):
    print(x)

#print(reverse table of 5 )
for x in range(50,4,-5):
    print(x)

#break statement for python

#for x in range(5):
   # if x == 3:
      # break
#print(x)

for x in range(5):
    if x == 3:
        break
    print(x) #0,1,2


for x in range(1,6):
    print(x)  #1,2,3
    if x == 3:
        break

for x in range(5,0,-1):
    print(x) #5,4,3,2
    if x == 2:
        break

#continue statement with for loop

for x in range(1,6):
    if x == 3:
        continue
    print(x) #1 2 4 5

for x in range(5,0,-1):
    if x==3:
        continue
    print(x) #5,4,2,1S


