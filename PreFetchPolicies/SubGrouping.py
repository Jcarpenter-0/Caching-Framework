import ObjectInfo.Object
import ObjectInfo.GroupInfo
from sklearn.cluster import DBSCAN
import numpy as np
# Hold a history of N, use DBScan to make a history

class SubGrouping:

    def __init__(self, library):
        self.LibraryDict = library
        self.Predictions = []
        self.LogFilePath = './tmp/subgroupingPredictions.txt'

    def Log(self):
        logFileDS = open(self.LogFilePath, 'w')

        for predictionObjectID in self.Predictions:
            logFileDS.write(str(predictionObjectID) + '\n')

        logFileDS.flush()
        logFileDS.close()

    # Request an item and place into cache if able and not already in
    def RequestItem(self, cacheObj):

        Coords = []
        ObjectIds = []

        for objId in cacheObj.Cache:
            ObjectIds.append(objId)
            Coords.append(cacheObj.Cache[objId].Traits)

        clustering = DBSCAN(eps=1, min_samples=3).fit(Coords)

        print('Cache Coordinate Locations:{}'.format(Coords))

        clusterIds = np.unique(clustering.labels_)

        print('Sub Groups Identified:{} | {}'.format(len(clusterIds)-1,clusterIds))

        cluster = []

        for clusterId in clusterIds:
            cluster.append(dict())

        for index, label in enumerate(clustering.labels_):

            if label == -1:
                pass
            else:
                # add to a subspace

                cluster[label][ObjectIds[index]] = cacheObj.Cache[ObjectIds[index]]

        # for each cluster, make an object space, then pick elements from them

        # get cluster with highest density, select from that at a higher rate

        for clusterId in clusterIds:

            if clusterId != -1:

                # get a space informed by the elements in the cache as a request history
                objSpace = ObjectInfo.GroupInfo.MakeObjectSpace(cluster[clusterId])

                # from this space, pick a random valid point
                soughtItemsTraits = objSpace.getRandomPoint()

                # find an existing object in the object library (eg: all possible objects) that is close to the desired traits
                resolvedObjectID = ObjectInfo.GroupInfo.GetClosestMedia(self.LibraryDict, ObjectInfo.Object.Object(-1, None,
                                                                                                                   soughtItemsTraits))

                # request the item, place it in the cache
                if resolvedObjectID is not None and resolvedObjectID not in cacheObj.Cache:
                    print('Predicted and cached:' + str(resolvedObjectID))

                    # log the prediction data
                    self.Predictions.append(resolvedObjectID)

                    # put it in the back of the cache or regular

                    cacheObj.Cache.popitem(last=False)
                    cacheObj.Cache[resolvedObjectID] = self.LibraryDict[resolvedObjectID]
                    cacheObj.AdmitsIntoCache += 1

                    # cacheObj.EvictionPolicy.Evict(self.LibraryDict[resolvedObjectID], True, cacheObj)
