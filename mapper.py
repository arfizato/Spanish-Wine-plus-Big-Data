import sys
from datetime import datetime
 
for line in sys.stdin:
    data = line.strip().split(",")
    if len(data) == 7:
        winery, wine, year, rating, numreviews, region, price = data
        print ("{0}\t{1}\t{2}\t{3}".format(winery, price, rating, numreviews))
 
 
