import csv

planetsList=[]
planetDiaList=[]
planetDistList=[]
planetGvtList=[]
planetDaylist=[]
planetTemplist=[]
planetNumMoonlist=[]
planetMasslist=[]

openfile = open('planeten.csv')
with openfile as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    next(readCSV)
    for row in readCSV:
        planetsList.append(row[0])
        planetDiaList.append(row[1])
        planetDistList.append(row[2])
        planetGvtList.append(row[3])
        planetDaylist.append(row[4])
        planetTemplist.append(row[5])
        planetNumMoonlist.append(row[6])
        planetMasslist.append(row[7])

planetsListnum = range(10)
infoTxt = ', '.join('% s = % s' % i for i in zip(planetsList, planetsListnum))
print (infoTxt)

planetInput = int(input("Bitte geben Sie eine Nummer zwischen 0 und 8: "))

planetDia = planetDiaList[planetInput]
planetName = planetsList[planetInput]
planetDistSun = planetDistList[planetInput]
planetGravity = planetGvtList[planetInput]
planetDay = planetDaylist[planetInput]
planetTemp = planetTemplist[planetInput]
planetNumMoon = planetNumMoonlist[planetInput]
planetMass = planetMasslist[planetInput]

#planets distance from earth
planetDistEarth = str (int(planetDistSun) - int(planetDistList[3]))
#diameter ratio to earth
planetScale2Earth = str( round(int(planetDia) / int(planetDiaList[3]),1 ))

#-----------------------------

if float(planetScale2Earth) < 1:
    planetScale2EarthTxt = " mal schmaler als die Erde."
else:
    planetScale2EarthTxt = " mal breiter als die Erde."

print ("Der Durchmesser von " + planetName + ": " + planetDia  + " km.")
if planetInput != 0:
    print ("Die Entfernung von " + planetName + " zur Sonne: " + planetDistSun +" Millionen km.")

else:
    pass

if planetInput != 3:
    print ("Die Entfernung von " + planetName + " zur Earth: " + planetDistEarth + " Millionen km.")
    print ("Das Durchmesserverhältniss von " + planetName + " zur Erde: " + planetScale2Earth + " " + planetScale2EarthTxt+".")
else:
    pass

print ("Die Schwerkraft von " + planetName + ": " + planetGravity + " m/s2.")

if planetInput != 0:
    print ("Ein Tag im " + planetName + " ist etwa: " + planetDay + " Stunden.")
    print ("Die mittlere Temperatur im " + planetName + " ist etwa: " + planetTemp + " C.")
    if int(planetNumMoon) <= 1:
        print (planetName + " hat " + planetNumMoon + " Monde.")
    else:
        print (planetName + " hat " + planetNumMoon + " Monde.")

    print ("Die Masse von " + planetName + " ist etwa " + planetMass + " (10 hoch 24 kg).")
else:
    pass
