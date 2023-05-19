# manin.py
# 衛星画像取得する範囲を指定
AREA =  [
  [
    139.0240751,
    36.1879383
  ],
  [
    139.0570341,
    34.7880413
  ],
  [
    140.8093534,
    34.8060848
  ],
  [
    140.8642851,
    36.1591156
  ],
  [
    139.0240751,
    36.1879383
  ]
]

from geojson import Polygon
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt 
m=Polygon([AREA])

# GeoJSON ファイルを出力
object_name = 'map'
import json
with open(str(object_name) +'.geojson', 'w') as f:
    json.dump(m, f)


hogejson = geojson_to_wkt(read_geojson(str(object_name) +'.geojson'))