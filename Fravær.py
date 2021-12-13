elever = []
NumberOf = int(input('Hvor mange elever: '))
half = len(elever) / 2
for x in range(NumberOf):
    add = input(str('Legg til en elev: '))
    elever.append(add)


HvemHer = []
NumberOf = int(input('Hvor mange er idag? '))
half = len(HvemHer) / 2
for x in range(NumberOf):
    add = input(str('Hvem er her i dag? '))
    HvemHer.append(add)

print(f"Okei så alle elevene i klasserommet er {elever}", "og de som er her i dag er", HvemHer)






    #getname = input(str('enter your letter: '))
#if students.count(getname) > 0:
    #index = students.index(getname)
    #if index >= half:
        #print("Excusably late")
   # else:
       # print("Not Excusably late")
#else:
    #print("Absent")