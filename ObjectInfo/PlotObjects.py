import json
import matplotlib.pyplot as plt

# simply create a basic scatter plot of where each object resides. NOTE CAN ONLY WORK IN 1D, 2D, 3D

OBJECTFILES = ['ObjectInfo.txt']

XAxisVals = []
YAxisVals = []

for filePath in OBJECTFILES:
    objectDataFDS = open(filePath)

    objectDataRaws = objectDataFDS.readlines()

    # for each Json object parse out the information
    for rawJson in objectDataRaws:
        reqObj = json.loads(rawJson)

        XAxisVals.append(reqObj['Traits'][0])
        YAxisVals.append(reqObj['Traits'][1])


plt.scatter(XAxisVals,YAxisVals)
plt.show()


