#initialization 
#while (condition):
#statement
#increment/decrement

#program1
#print(1 to 5)
i1=1
while(i1 <= 5):
    print(i1)
    i1=i1+1

#print hello 3 times

i=1
while(i <=3):
    print("hello")
    i=i+1

#print(5 to 1)
i2=5
while(i2 >=1):
    print(i2)
    i2=i2-1

#table of 2
i3=1
while(i3 <=10):
    print(i3 * 2)
    i3=i3+1

#
#reverse table of 2
i3=10
while(i3 >=1):
    print(i3 * 2)
    i3=i3-1

#break statement with for loop

q=1
while(q <=5):
    if(q==3):
        break
    print(q) #1,2
    q=q+1

q=1
while(q <= 5):
    print(q) #1,2 ,3
    if(q==3):
        break
    q=q+1

#continue statement with while loop

x = 1
while(x <=5):
    if(x==3):
        x=x+1
        continue
    print(x) #1 2 4 5
    x=x+1