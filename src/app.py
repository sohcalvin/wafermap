import numpy as np
from models.wafermap import WaferMap
import json

# pattern1 = [[35,34], [34,35], [33,32],[33,32],[35,36],[36,36],[36,38],[35,36],[36,36],[36,38],[39,38],[36,35],[34,35],[34,36],[34,37]]

pattern1 = [[i,i] for i in (range(25,40))]

for i in range(1,10):
    waferid = "wafer{0}".format(i)
    waferMap = WaferMap(waferid, title="Pattern1")
    waferMap.initMap(100,100,pattern1)
    waferMap.save("data/{0}".format(waferid))

# waferMap2 = WaferMap.load("t.txt")

# jsonData = waferMap2.jsonData();
# print(json.dumps(jsonData))


