import ObjectInfo.Object
import ObjectInfo.GroupInfo
# simply randomly select an item from the library

class SimpleRandom:

    def __init__(self, library):
        self.LibraryDict = library

    # Request an item and place into cache if able and not already in
    def RequestItem(self, cacheObj):

        # get a space informed by the elements in the whole library
        objSpace = ObjectInfo.GroupInfo.MakeObjectSpace(self.LibraryDict)

        # from this space, pick a random valid point
        soughtItemsTraits = objSpace.getRandomPoint()

        # find an existing object in the object library (eg: all possible objects) that is close to the desired traits
        resolvedObjectID =  ObjectInfo.GroupInfo.GetClosestMedia(self.LibraryDict, ObjectInfo.Object.Object(-1,None,soughtItemsTraits))

        # request the item, place it in the cache
        if resolvedObjectID is not None and resolvedObjectID not in cacheObj.Cache:
            print('Predicted and cached:' + str(resolvedObjectID))
            cacheObj.EvictionPolicy.Evict(self.LibraryDict[resolvedObjectID],True,cacheObj)
