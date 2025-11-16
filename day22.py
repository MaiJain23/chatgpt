#program

numbers=[1,2,3,4,5,6]
e=list(map(lambda x:x*x,numbers))
print(e)

#program 2

#names =["Rani Mukhargi", "Sonali Bendre", "Aish Roy", "Alia Bhatt"]
#print(names[0]) #Rani Mukhargi
#print(names[0].split(" ")[0]) #Rani

#for Loop


names = ["Rani Mukhargi", "Sonali Bendre", "Aish Roy", "Alia Bhatt"]

firstNames = []
for x in names:
    firstNames.append(x.split(" ")[0])

print(firstNames)

#map

e2=list(map(lambda fn:fn.split(" ")[0],names))
print(e2)

#list comprehension

e3=[fn.split(" ")[0] for fn in names]
print(e3)


#program 2

numbers=[1,2,3,4,2,3,4,5]
e4=list(filter(lambda x: x%2==0,numbers))
print(e4)

e5=[x for x in numbers if x % 2==0]
print(e5)
#program 3

names=["John","","Alice","","Bob"]
o= filter(lambda str:len(str) > 0,names)
print(list(o))

students=[
    {
        "fn":"mayuri",
        "ln":"kalegore",
        "age":25
    },
    {
        "fn":"atul",
        "ln":"kalegore",
        "age":35

    },
    {
        "fn":"mayu",
        "ln":"jain",
        "age":32
    }
]

e6=[dicA for dicA in students if dicA["age"]>30]
print(e6)

