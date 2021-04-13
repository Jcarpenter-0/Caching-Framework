# Run tests
import Cache
import ObjectInfo.Object
import AdmissionPolicies.AdmitAll
import EvictionPolicies.LRU
import PreFetchPolicies.Heuristic
import PreFetchPolicies.SubGrouping


# Testing Paras
Tracefile = './Traces/BiasTrace.txt'
ObjectMappingFile = './ObjectInfo/ObjectInfo.txt'
DELIMITER = ','
VERBOSE = True
# Cache size in entries
CacheSize = 10

ObjectMapping = ObjectInfo.Object.BuildObjectDict(ObjectMappingFile)

CacheSystem = Cache.Cache(CacheSize,
                          AdmissionPolicies.AdmitAll.AdmitAll()
                          ,EvictionPolicies.LRU.LRU()
                          ,PreFetchPolicies.SubGrouping.SubGrouping(ObjectMapping)
                          )

#CacheSystem = Cache.Cache(CacheSize,
#                          AdmissionPolicies.AdmitAll.AdmitAll()
#                          ,EvictionPolicies.LRU.LRU()
#                          ,None
#                          )

# Far future, multiple caches, multiple tests
# Cache systems to test = [(AdmitAll(), LRU(), Hueristic()),(),()]

def main():

    # Load the trace
    traceFile = open(Tracefile, 'r')

    # feed into the system
    line = traceFile.readline()

    while line is not None:

        line = line.replace('\n','')

        if len(line) <= 0:
            line = None

        request = None

        if line is not None:
            # map to object traits
            request = ObjectMapping[int(line)]

        CacheSystem.processIncoming(request)

        line = traceFile.readline()

        if len(line) <= 0:
            line = None

    # finish
    traceFile.close()

    # print the data
    print('Hit rate:' + str(CacheSystem.Hits/(CacheSystem.Hits + CacheSystem.Misses)))
    print('Misses:' + str(CacheSystem.Misses))
    print('Evictions:' + str(CacheSystem.Evicts))

    if CacheSystem.PreFetchPolicy is not None:
        CacheSystem.PreFetchPolicy.Log()



if __name__ == '__main__':
    main()