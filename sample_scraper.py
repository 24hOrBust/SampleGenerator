import json
from pymongo import MongoClient

client = MongoClient("mongodb://admin:VXPBVXMOOBZGNPQB@portal-ssl866-34.bmix-dal-yp-0f89b96c-d9b1-4f40-b8da-1ef66b25ead1.4068962045.composedb.com:57337,portal-ssl854-33.bmix-dal-yp-0f89b96c-d9b1-4f40-b8da-1ef66b25ead1.4068962045.composedb.com:57337/compose?authSource=admin&ssl=true")
#client = MongoClient("localhost:27017")

start_lat = int(39.382280 * 1000000)
start_long = int(-123.668742 * 1000000)
end_lat = int(39.391414 * 1000000)
end_long = int(-123.658898 * 1000000)

deg_per_m = 0.000009 * 1000000
meter_step = 20

# forest_y1a = 42.948426
# forest_x1a = -73.618232
# forest_y2a = 42.947527
# forest_x2a = -73.617941
# m1 = (forest_y2a - forest_y1a) / (forest_x2a - forest_x1a)

# forest_y1b = 42.948143
# forest_x1b = -73.616585
# forest_y2b = 42.947326
# forest_x2b = -73.615990
# m2 = (forest_y2b - forest_y1b) / (forest_x2b - forest_x1b)

client.fuel_scan.messurements.remove()

for lat in range(start_lat, end_lat, int(meter_step * deg_per_m)):
    for lng in range(start_long, end_long, int(meter_step * deg_per_m)):
        d = {}
        d['position'] = {
            'lat' : lat / 1000000,
            "lng" : lng / 1000000
        }
        d['classification'] = 'Unknown'
        d['sample'] = 'True'
            
        client.fuel_scan.messurements.insert_one(d)