import random
import ObjectInfo.Object

# Info gathered on groups of objects
class ObjectSpace:

    # axisDimensions is a [(upper,lower)] for each dimension, eg: 2d would be [3,3]
    def __init__(self, coreCoordinates, axisDimensions):
        self.Core = coreCoordinates
        self.AxisDimensions = axisDimensions

    def getRandomPoint(self):

        coords = []

        for i in range(0,len(self.Core)):
            lowerBound = int(self.Core[i] - (self.AxisDimensions[i]/2))
            upperBound = int(self.Core[i] + (self.AxisDimensions[i]/2))

            coords.append(random.randint(lowerBound,upperBound))

        return coords


def MakeObjectSpace(objectDict):

    # go through the dict,
    avgObject = GetAverageMedia(objectDict)

    # get furthest distances of objects
    distance = GetFurthestDistance(objectDict)

    objectSpaceCoords = []

    # for each dimension
    for dimension in range(0,len(avgObject.Traits)):
        objectSpaceCoords.append(distance)

    newSpace = ObjectSpace(avgObject.Traits,objectSpaceCoords)

    return newSpace


def GetClosestMedia(objDict, soughtMedia):
    closestMedia = None
    smallestDist = 999

    for mediaItem in objDict:
        dist = soughtMedia.Compare(objDict[mediaItem])
        if (dist <= smallestDist):
            closestMedia = mediaItem
            smallestDist = dist

    #closestMedia.RequestCount = closestMedia.RequestCount + 1
    return closestMedia

def GetClosestMediaWithTolerance(self, soughtMedia, tolerance):
    closetFound = self.GetClosestMedia(soughtMedia)

    if(closetFound is not None):
        if(soughtMedia.Compare(closetFound) > tolerance):
            closetFound = None

    return closetFound

def GetFurthestMedia(objDict, soughtMedia):

    largestDist = -1
    farthestMedia = None

    for mediaItem in objDict:
        dist = soughtMedia.Compare(mediaItem)
        if (dist >= largestDist):
            farthestMedia = mediaItem
            largestDist = dist

    return farthestMedia

def GetAverageMedia(objDict):
    hypotheticalNextMediaitem = ObjectInfo.Object.Object(-1,None,[0] * 2)

    for lastMedia in objDict:
        genreIndex = 0

        for weight in objDict[lastMedia].Traits:
            # Add the weight
            hypotheticalNextMediaitem.Traits[genreIndex] = hypotheticalNextMediaitem.Traits[genreIndex] + weight

            genreIndex = genreIndex + 1

    # Now averages all the values
    for newWeight in hypotheticalNextMediaitem.Traits:
        hypotheticalNextMediaitem.Traits[
            hypotheticalNextMediaitem.Traits.index(newWeight)] = newWeight / (
            len(objDict))

    return hypotheticalNextMediaitem

#Distance/Grouping Ops

def GetFurthestDistance(objDict):
    largestDist = -1

    for obj1 in objDict:
        for obj2 in objDict:

            dist = objDict[obj1].Compare(objDict[obj2])

            if(dist > largestDist):
                largestDist = dist

    return largestDist

def FilterByAMediaItem(objDict, object, distance):
    #Go through each item in the list and simply remove them if too far from the coordinate

    filteredGroup = objDict.copy()

    for obj in objDict:
        if(object.Compare(objDict[obj]) > distance):
            del filteredGroup[obj]

    return filteredGroup