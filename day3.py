#list

names = ["rakhi","mahesh","sonali","sanjay"]
print(names) # we get list ['rakhi', 'mahesh', 'sonali', 'sanjay']
print(type(names))  #<class 'list'>

numbers = [11,22,33,44]
print(numbers)
print(type(numbers))
#it can store multiple data in list
info = ["rakhi","sawant",34,45.6,True]
print(info)

#program 2

cities = ["chennai","manglore","delhi",'pune']
print(cities[0])  #chennai
print(cities[1])  #manglore
print(cities[2])  #delhi
print(cities[3])  #pune

e = len(cities)
print(e)  #4

lastIndex = len(cities) - 1
print(lastIndex) #3

#program 3

countries = ["india", "shrilanka","dubai","america"]
print(countries)

#for loop
#for x in range(startIndex,endIndex,stepsize):
#print(x)

for x in range(1,5):
    print(x)

#flowers

Flowers = ["lily","rose","lotus","jasmine","sunflower"]
for x in range(len(Flowers)):
   # print(x)  #0,1,2,3,4
   print(Flowers[x])

animals = ["tiger","lion","elephant","rabbit"]
print(animals)
print(len(animals)) #4

i1=0
while i1 < len(animals):
    print(animals[i1])
    i1 = i1 + 1


