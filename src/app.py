import numpy as np
from models.wafermap import WaferMap
import json

# pattern1 = [[35,34], [34,35], [33,32],[33,32],[35,36],[36,36],[36,38],[35,36],[36,36],[36,38],[39,38],[36,35],[34,35],[34,36],[34,37]]

pattern1 = [[i,i] for i in (range(25,40))]

waferMap = WaferMap("wafer1", title="Pattern1")
waferMap.initMap(100,100,pattern1)

# print(waferMap)

jsonData = waferMap.jsonData()
print(json.dumps(jsonData))
# json.dumps(your_data, ensure_ascii=False)


