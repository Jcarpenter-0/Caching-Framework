import ObjectInfo.Object
import ObjectInfo.GroupInfo
import random

# create trace file by determining group locations to target with radii and then attach a % chance for that region

OBJECTINFOFILE = './../ObjectInfo/ObjectInfo.txt'

# load in object info
ObjectData = ObjectInfo.Object.BuildObjectDict(OBJECTINFOFILE)
ObjectsInfoSpace = ObjectInfo.GroupInfo.MakeObjectSpace(ObjectData)

# 2,1
# 3,4

CoreXBase = ObjectsInfoSpace.Core[0]
CoreYBase = ObjectsInfoSpace.Core[1]
AxisDim = ObjectsInfoSpace.AxisDimensions[0]/4

Cores = [
    [CoreXBase + AxisDim, CoreYBase + AxisDim],
    [CoreXBase - AxisDim, CoreYBase + AxisDim],
    [CoreXBase - AxisDim, CoreYBase - AxisDim],
    [CoreXBase + AxisDim, CoreYBase - AxisDim]
]

Radii = [7,3,3,3]
Probs = [80,85,95,100]

TRACEOUTPUTFILE = './BiasTrace.txt'
TRACELENGTH = 100000

# for length of trace
traceFile = open(TRACEOUTPUTFILE,'w')

for i in range(0,TRACELENGTH):

    # roll a number, select the group, then get an item from that group
    groupProb = random.randint(0,100)

    # get element from that group
    groupNum = -1

    for index, prob in enumerate(Probs):
        if groupProb <= prob:
            groupNum = index
            break

    # get group data
    core = Cores[groupNum]
    radius = Radii[groupNum]

    # get an object
    sought = ObjectInfo.Object.Object(-1,None,core)

    subgroupDict = ObjectInfo.GroupInfo.FilterByAMediaItem(ObjectData, sought, radius)
    subspace = ObjectInfo.GroupInfo.MakeObjectSpace(subgroupDict)

    soughtCoords = ObjectInfo.Object.Object(-1,None,subspace.getRandomPoint())

    objectId = ObjectInfo.GroupInfo.GetClosestMedia(subgroupDict, soughtCoords)

    traceFile.write(str(objectId) + '\n')

traceFile.flush()
traceFile.close()