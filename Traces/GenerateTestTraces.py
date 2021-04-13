import ObjectInfo.Object
import ObjectInfo.GroupInfo
import random
# create a test trace

OBJECTINFOFILE = './../ObjectInfo/ObjectInfo.txt'
TRACEOUTPUTFILE = './Trace.txt'
TRACELENGTH = 100000

# Read in the object definitions file and create a trace
objects = ObjectInfo.Object.BuildObjectDict(OBJECTINFOFILE)
traceFile = open(TRACEOUTPUTFILE,'w')

for i in range(0,TRACELENGTH):

    objectId = random.randint(0,len(objects)-1)
    traceFile.write(str(objectId) + '\n')

traceFile.flush()
traceFile.close()
