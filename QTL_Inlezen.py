import re
import scipy.stats as stats

## Openen  en inlezen Waardenbestand
WaardenFile = open("QTLwaarden(1).qua", "r").readlines()


## Filteren van Waardendata tot een lijst met alleen waarden.
WaardenLijst = []
for line in WaardenFile[8:]:
    RawWaarden = line.replace("\n", "").replace("-","0")
    SplitWaarden = RawWaarden.split("\t")
    WaardenLijst.append(SplitWaarden[1])

IntWaardenLijst = []
IntWaardenLijst = [round(float(x),10) for x in WaardenLijst]                                                            #Maakt van stringlijst een intlijst


## Openen en inlezen van Markerbestand.
with open("QTLgroepen.loc", "r") as MarkerFile:

## Markerdata op 1 regel, waarna gesplit in een lijst.
    RawMarkerData = MarkerFile.read().replace("\n", "").replace(" ", "").replace("\t", "")
    #print(RawMarkerData)

    SplitMarkerData = RawMarkerData.split("(a,b)")
    RawMarkerLijst = SplitMarkerData[1:]
    #print(RawMarkerLijst)

ANOVALijst = []
## Wegfilteren van ongewenste karakters.
for item in RawMarkerLijst:
    NoCapitals = re.sub(r'[A-Z].*', '', item)
    NoAB = re.sub(r'[c-z].*', '', NoCapitals)
    NoNumber = re.sub(r'[0-9]', '', NoAB)
    NoExtra = NoNumber.replace(";","")
    print(NoExtra)

    print(len(NoExtra))

## Doorloop abseq en voegt waarde toe.
    LijstA = []
    LijstB = []


    WaardenLijstindex = 0
    for ABitem in NoExtra:
        if ABitem == "a":
            LijstA.append(IntWaardenLijst[WaardenLijstindex])
            WaardenLijstindex = WaardenLijstindex + 1
            #print(LijstA)
        elif ABitem == "b":
            LijstB.append(IntWaardenLijst[WaardenLijstindex])
            WaardenLijstindex = WaardenLijstindex + 1
            #print(LijstB)
        else:
            WaardenLijstindex = WaardenLijstindex + 1
            continue

    #print(LijstA)
    #print(LijstB)
    ANOVALijst.append(stats.f_oneway(LijstA, LijstB)))

print(ANOVALijst)

