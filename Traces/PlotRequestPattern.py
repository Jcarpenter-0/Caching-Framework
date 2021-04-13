import json
import ObjectInfo.Object
import matplotlib.pyplot as plt

# simply create a basic scatter plot of where each object resides. NOTE CAN ONLY WORK IN 1D, 2D, 3D

ObjectDataFile = '../ObjectInfo/ObjectInfo.txt'
TraceFile = 'BiasTrace.txt'
TraceFile = '../tmp/subgroupingPredictions.txt'
TraceFileDS = open(TraceFile, 'r')

ObjectsInfo = ObjectInfo.Object.BuildObjectDict(ObjectDataFile)

XAxisVals = []
YAxisVals = []

# for each line in the trace file, link the object and then get the coordinates
TraceLines = TraceFileDS.readlines()

TraceFileDS.close()

for line in TraceLines:
    # get the object id from the line
    objID = int(line.replace('\n',''))

    # get object from listing
    obj = ObjectsInfo[objID]

    # add coords
    XAxisVals.append(obj.Traits[0])
    YAxisVals.append(obj.Traits[1])


plt.scatter(XAxisVals,YAxisVals)
plt.show()


