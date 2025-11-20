#generators

def get_numbers():
    return 1
    return 2
    return 3

print(get_numbers()) # 1
#return is the last statement of any generator

def get_numbers2():
    return [1,3,4,5]
print(get_numbers2)

# A generator is a special type of function , which returns more than one value at a 
#time

def get_numbers3():
    yield 1
    yield 2
    yield 3
    yield 4

gen = get_numbers3()
print(gen)

e1 = next(gen)
print(e1)
print(next(gen))
print(next(gen))
print(next(gen))

#print(next(gen))
#until it hits the last yield value

def infinite_generator():
    n = 1
    while True:
        yield n
        n = n + 1

gen2 = infinite_generator()
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))