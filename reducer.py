#!/usr/bin/python
 
import sys
 
totalPrice = 0
numberOfItems = 0
totalRating=0
totalReviews=0
 
oldKey = None
 
 
print ("{:<60} {:<20} {:<20} {:<20}|| {:<20} {:<20}\n\n".format( "Winery Name","Total Revenue","Number Of Items","Average Revenue","Average Rating","Total Reviews"))
 
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    #print(len(data_mapped),data_mapped)
    if len(data_mapped) != 4:
        # Something has gone wrong. Skip this line.
        continue
 
    thiskey, currentPrice, currentRating, numberOfReviews = data_mapped
 
    if oldKey and oldKey != thiskey:
        print ("{:<60} {:<20} {:<20} {:<20}|| {:<20} {:<10}".format( oldKey,totalPrice,numberOfItems,totalPrice/numberOfItems,totalRating/numberOfItems,totalReviews))
        oldKey = thiskey;
        totalPrice = 0
        numberOfItems=0
        totalRating=0
        totalReviews=0
 
 
    oldKey = thiskey
    numberOfItems+=1
    totalPrice += float(currentPrice)
 
    totalRating+=float(currentRating)
    totalReviews+=int(numberOfReviews)
 
 
if oldKey != None:
    print ("{:<60} {:<20} {:<20} {:<20}|| {:<20} {:<10}".format( oldKey,totalPrice,numberOfItems,totalPrice/numberOfItems,totalRating/numberOfItems,totalReviews))
