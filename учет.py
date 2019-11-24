import json
lol = {}
with open("студенты.json", "r", encoding="utf-8") as f:
    lol = json.load(f)
    #print(lol)
def Minu(lol):
    a=int(input("1:Напечатать всех\n2:Напечатать отличников\n3:напичатать неуспевающих\n4:добавить\n5:редактировать\n6:удалить\n7:Выход"))
    if a==1:
        PrintAll(lol)
    if a == 7:
        for i in range(1):
            pass
            break
    if a==5:
        redakt(lol)
    if a == 4:
        plus(lol)
    if a == 6:
        delete(lol)
    if a == 2:
        Print5(lol)
    if a == 3:
        Print345(lol)
def Print5(lol):
    for i in lol["all"]:
        с=i["оценки"]
        flag=True
        for a in с:
            if a != 5:
                flag=False
        if flag == True:
            print(i["имя"]+" "+i["фамилия"]+" "+"отличник")
        Minu(lol)
def Print345(lol):
    for i in lol["all"]:
        с=i["оценки"]
        flag=True
        for a in с:
            if a == 2:
                flag=False
        if flag == False:
            print(i["имя"]+" "+i["фамилия"]+" "+"неуспевающий")
        Minu(lol)
def delete(lol):
    a=int(input("введите номер ученика"))
    del lol["all"][a-1]
    file = open("студенты.json",mode="w",encoding="utf-8")
    file.write(json.dumps(lol, ensure_ascii=False))
    file.close
    print(lol)
    Minu(lol)
def plus(lol):
    g = {}
    o=input("введите номер нового ученика")
    a=input("введите имя нового ученика")
    m=input("введите фамилию нового ученика")
    p=input("введите новое отчество ученика")
    j=input("введите название группы нового ученика")
    g["номер"]=o
    g["имя"]=a
    g["фамилия"]=m
    g["отчество"]=p
    g["группа"]=j
    g["оценки"]=[]
    lol["all"].append(g)
    file = open("студенты.json",mode="w",encoding="utf-8")
    file.write(json.dumps(lol, ensure_ascii=False))
    file.close
    Minu(lol)
def redakt(lol):
    p=int(input("введите номер ученика"))
    c=(lol["all"][p-1])
    i=int(input("1:изменить имя\n2:изменить фамилию\n3:изменить отчество\n4:изменить группу\n5:добавить оценки\n6:удалить оценки\n7:назад\n "))
    if i == 1:
        a=input("введите новое имя: ")
        c["имя"]=a
        file = open("студенты.json",mode="w",encoding="utf-8")
        file.write(json.dumps(lol, ensure_ascii=False))
        file.close
        Minu(lol)
    if i == 2:
        a=input("введите новую фамилию: ")
        c["фамилия"]=a
        file = open("студенты.json",mode="w",encoding="utf-8")
        file.write(json.dumps(lol, ensure_ascii=False))
        file.close
        Minu(lol)
    if i == 3:
        a=input("введите новую отчество: ")
        c["отчество"]=a
        file = open("студенты.json",mode="w",encoding="utf-8")
        file.write(json.dumps(lol, ensure_ascii=False))
        file.close
        Minu(lol)
    if i == 4:    
        a=input("введите новое название группы: ")
        c["группа"]=a
        file = open("студенты.json",mode="w",encoding="utf-8")
        file.write(json.dumps(lol, ensure_ascii=False))
        file.close
        Minu(lol)
    if i == 5:
        a=int(input("введите оценку которую хотите поставить"))
        r=c["оценки"]
        r.append(a)
        c["оценки"]=r
        file = open("студенты.json",mode="w",encoding="utf-8")
        file.write(json.dumps(lol, ensure_ascii=False))
        file.close
        Minu(lol)
    if i == 6:
        print(c["оценки"])
        a=int(input("введите номер оценки которую хотите убрать"))
        r=c["оценки"]
        del r[a-1]
        c["оценки"]=r
        file = open("студенты.json",mode="w",encoding="utf-8")
        file.write(json.dumps(lol, ensure_ascii=False))
        file.close
        Minu(lol)
    if i == 7:
        exit()
        Minu(lol)
def PrintAll(lol):
    #print(lol)
    for i in lol["all"]:
        print(str(i["номер"])+"\t"+str(i["имя"])+"\t"+str(i["фамилия"])+"\t"+str(i["отчество"])+"\t"+str(i["группа"])+"\t"+str(i["оценки"]))
    Minu(lol)
Minu(lol)