import math

#using haversine formula
def distance(loc1,loc2):

	radius = 6371
	
	lat1 = (loc1['lat']*math.pi/180)
	lat2 = (loc2['lat']*math.pi/180)

	lon1 = (loc1['lon']*math.pi/180)
	lon2 = (loc2['lon']*math.pi/180)

	inside_sqrt = ((math.sin((lat2-lat1)/2))**2)+math.cos(lat1)*math.cos(lat2)*((math.sin((lon2-lon1)/2))**2)
	# print(inside_sqrt)
	d = 2*radius*math.asin(math.sqrt(inside_sqrt))
	return d*1000
	


