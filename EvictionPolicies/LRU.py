# LRU eviction policy


class LRU:

    # Select an entry and eject it
    def Evict(self, requestedObject, admitDecision, cacheObj):

        # since the ordered dict is expected order pop and remove at the end
        if len(cacheObj.Cache) <= cacheObj.Capacity and admitDecision and requestedObject.ObjectID not in cacheObj.Cache:
            # Add item
            cacheObj.Cache[requestedObject.ObjectID] = requestedObject
            cacheObj.AdmitsIntoCache += 1

        while len(cacheObj.Cache) > cacheObj.Capacity:

            # evict until open space
            cacheObj.Cache.popitem(last=False)

            cacheObj.Evicts += 1

