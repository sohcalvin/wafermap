import numpy as np
from models.wafermap import WaferMap

pattern1 = [[5,4], [4,5], [3,2],[3,2],[5,6],[6,6],[6,8],[5,6],[6,6],[6,8],[9,8],[6,5],[4,5],[4,6],[4,7]]

waferMap = WaferMap()
waferMap.initMap(15,15,pattern1)

print(waferMap)


