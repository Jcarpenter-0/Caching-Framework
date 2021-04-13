import ObjectInfo.Object
import random
# Generate test object definitions

# Pattern is
# Object ID, Size, Title, GenreWeights

NumberOfObjects = 100
RangeOfWeights = 10
NumberOfWeights = 2
# number to add to the generated weight
WeightOffsets = [0,0]

OBJECTFILENAME = './ObjectInfo.txt'

objectInfoFile = open(OBJECTFILENAME,'w')

for i in range(0,NumberOfObjects):

    # create the random array
    numberArray = []

    for num in range(0,NumberOfWeights):
        weight = random.randint(-1*RangeOfWeights,RangeOfWeights) + WeightOffsets[num]
        numberArray.append(weight)

    newObject = ObjectInfo.Object.Object(i,None,numberArray)

    objectInfoFile.write(newObject.ToString() + '\n')


objectInfoFile.flush()
objectInfoFile.close()