students =[
    {
        "firstname" : "mayuri",
        "lastname" : "kalegore",
        "age" : 25,
        "skills" : ["python","sql","excel"],
        "marks" :{"maths":56,"science":76,"english":67}
    },
    {
        "firstname" : "mayu",
        "lastname" : "jain",
        "age" : 45,
        "skills" : ["python","sql","js"],
        "marks" :{"maths":58,"science":75,"english":77}

    },
    {"firstname" : "mahel",
        "lastname" : "kale",
        "age" :34,
        "skills" : ["python","sql","excel"],
        "marks" :{"maths":65,"science":78,"english":89}
    },
    {
        "firstname" : "malti",
        "lastname" : "chahr",
        "age" : 25,
        "skills" : ["python","sql","excel"],
        "marks" :{"maths":45,"science":78,"english":47}
    }
]

#firstnames of all students

for x in students:
    print(x['firstname'])

#firstname and number of skills

for x in students:
    e = str(len(x["skills"]))
    print(f'{x['firstname']}:{e}')

#firstname + total number of marks
for x in students:
    total = x['marks']['maths'] + x['marks']['science'] + x['marks']['english']
    total =str(total)
    print(x['firstname'] +" "+total)

