import numpy as np

from models.wafermap import WaferMap

pattern1 = [[4,4],[5,4],[4,5],[4,6],[6,4]]
waferMap = WaferMap()
waferMap.initMap(9,8,pattern1)

print(waferMap)


