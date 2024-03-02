exam_pass =[{"name":"ekene", "exam_no":100},
            {"name":"dere", "exam_no":120},
            {"name":"sonia", "exam_no":130},
            {"name":"sylvia", "exam_no":140},
            {"name":"sandra", "exam_no":150} ]

x = input("enter your exam number: ")


pay=''

for i in exam_pass:
    if int(x) == i["exam_no"]:
        pay =f" hello {i['name']} \n {i['exam_no']}"
        break
    else:
        pay='pay your fees'


print(pay)