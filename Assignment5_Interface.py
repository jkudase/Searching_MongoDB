#
# Assignment5 Interface
# Name: Jayesh Uddhav Kudase
#

from pymongo import MongoClient
import os
import sys
import json
from math import sin,cos,radians,pow,atan2,sqrt

def FindBusinessBasedOnCity(cityToSearch, saveLocation1, collection):
    
    file1 = open(saveLocation1, "wb")
    for record in collection.find({'city': { "$regex" : cityToSearch, "$options" : "-i" }}):
        recordToInsert = record['name'].upper() + "$" + record['full_address'].replace('\n',',').upper() + "$"+ record['city'].upper() + "$"+ record['state'].upper() +"\n"
        strRecordToInsert = str(recordToInsert)
        file1.write(strRecordToInsert.encode('utf-8'))
    file1.close()
        

def FindBusinessBasedOnLocation(categoriesToSearch, myLocation, maxDistance, saveLocation2, collection):
        
    file2 = open(saveLocation2, "wb")
    lat1 = myLocation[0]
    lon1 = myLocation[1]

    for record in collection.find(projection = ['name', 'categories', 'latitude', 'longitude']):
        lat2 = record['latitude']
        lon2 = record['longitude']
        
        if(float(findDistance(float(lat2), float(lon2), float(lat1), float(lon1))) <= float(maxDistance)):
            for category in categoriesToSearch:
                if category in record['categories']:
                    file2.write(str(record['name'].upper()+ "\n").encode("utf-8"))
                    break
    file2.close()
    
def findDistance(lat2, lon2, lat1, lon1):
    
    R = 3959
    si1 = radians(lat1)
    si2 = radians(lat2)
    deltasi = radians(lat2 - lat1)
    deltalambda = radians(lon2- lon1)
    
    a = pow(sin(deltasi/2),2) + (cos(si1) * cos(si2) * pow(sin(deltalambda/2),2))
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    d = R * c
    
    return d
    