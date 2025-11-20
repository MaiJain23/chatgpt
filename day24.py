from functools import reduce

employees = [
    {"id": 1, "name": "John",   "age": 28, "salary": 45000, "department": "IT"},
    {"id": 2, "name": "Alice",  "age": 34, "salary": 72000, "department": "HR"},
    {"id": 3, "name": "Bob",    "age": 25, "salary": 38000, "department": "IT"},
    {"id": 4, "name": "David",  "age": 42, "salary": 96000, "department": "Finance"},
    {"id": 5, "name": "Sara",   "age": 30, "salary": 55000, "department": "HR"}
]

#extract 1st name of all employees

print(list(map(lambda emp:emp["name"],employees)))

#increase salary of all employees by 10%

#


#employee salary greater than 50

print("=========================================================")
above50000=list(filter(lambda emp:emp['salary']>50000,employees))
print(list(map(lambda emp:emp['name'],above50000)))


#employee of it department

print("===========================================================")
itdepartment=list(filter(lambda emp:emp['department'] == "IT",employees))
print(list(map(lambda emp:emp['name'],itdepartment)))