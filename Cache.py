import collections
# will be the cache class itself

# Based on this code https://www.kunxi.org/2014/05/lru-cache-in-python/

class Cache:

    def __init__(self, capacity, admitPolicy = None, evictPolicy = None, preFetchPolicy = None):
        self.Capacity = capacity
        self.Cache = collections.OrderedDict()
        self.Logicaltime = 0
        self.AdmissionPolicy = admitPolicy
        self.EvictionPolicy = evictPolicy
        self.PreFetchPolicy = preFetchPolicy

        self.Hits = 0
        self.Misses = 0
        self.TotalRequests = 0
        self.AdmitsIntoCache = 0
        self.Evicts = 0


    # object is requested
    def processIncoming(self, requestedObject):
        print('Request:' + str(requestedObject.ObjectID))

        admitCurrentObject = False

        # Is object in the cache?
        if requestedObject.ObjectID in self.Cache:
            # hit
            self.Hits += 1
            entryValue = self.Cache.pop(requestedObject.ObjectID)
            # update placement in ordered dict by reentering it
            self.Cache[requestedObject.ObjectID] = entryValue
        else:
            # miss
            self.Misses += 1
            # run admission
            admitCurrentObject = self.AdmissionPolicy.decideAdmission(requestedObject, self)


        # Run Evict Logic, may not need to run
        self.EvictionPolicy.Evict(requestedObject, admitCurrentObject, self)

        # Run Prefetch, may not need to run
        if self.PreFetchPolicy is not None:
            self.PreFetchPolicy.RequestItem(self)

        # update the logical time
        self.Logicaltime += 1

        # print cache state
        print('Logical Time:' + str(self.Logicaltime) + '|Hit Rate:' + str(self.Hits/(self.Hits + self.Misses)) + '|CacheLen:' + str(len(self.Cache)))
        print('Cache Entries:' + str(self.Cache.keys()))