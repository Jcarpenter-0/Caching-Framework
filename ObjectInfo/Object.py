import json
import math

class Object:

    def __init__(self, objectID, title, genreweights):
        self.Traits = genreweights
        self.ObjectID = objectID
        self.Title = title
        self.Size = 0

    def ToString(self):
        return json.dumps(self.__dict__)

    def Compare(self, compareItem):
        runningDist = 0
        index = 0
        for weight in self.Traits:
            runningDist = runningDist + (weight - float(compareItem.Traits[index]))
            index = index + 1

        return math.fabs(runningDist)

def BuildObjectDict(dictFile):

    objectFile = open(dictFile,'r')

    objsRaw = objectFile.readlines()

    objectFile.close()

    objDict = dict()

    for objRaw in objsRaw:
        object = JSONToMediaItem(objRaw)

        objDict.update({object.ObjectID : object})

    return objDict

def JSONToMediaItem(jsonData):

    dataFields = json.loads(jsonData)

    objectID = dataFields['ObjectID']
    dataWeights = dataFields['Traits']
    dataTitle = dataFields['Title']

    return Object(objectID,dataTitle,dataWeights)