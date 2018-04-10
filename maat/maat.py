import click
import math
from haversine import haversine
from mavconn import MAVLinkConnection


class Args:

    def __init__(self, ip, loc, system, component):
        self.ip_addr= ip
        self.lat=loc[0]
        self.long=loc[1]
        self.altitude=loc[2]
        self.loc = loc[0], loc[1], loc[2]
        self.mavsystem = system
        self.mavcomponent = component


def heartbeat():
    pass


def static_location(lat, long, alt):
    def ret_gps():
        return lat, long, alt
    return ret_gps


def global_position_handler(gps_func, reporter):
    #gps_func is what static_location returns
    def gps_handler(mavlinkconn, message):
        # destination location will get from message
        # ID and component also comes from message
        # gives these to the reporter
        pass
    return gps_handler


def global_position_int_handler(gps_func, reporter):
    pass


def printer(system, component, azimuth, elevation):
    #give as reporter
    # prints system.component: az, el (unicode degree)
    return 


def calculate_azimuth_elevation(source, dest):
    #inputs are two triples (tuples) with lat, long, altitude
    #return azimuth and elevation from source to dest
    if (type(source) != tuple) or (type(dest) != tuple):
        raise TypeError("Only tuples are supported as arguments")

    lat1 = math.radians(source[0])
    lat2 = math.radians(dest[0])

    diffLong = math.radians(dest[1] - source[1])

    x = math.sin(diffLong) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
            * math.cos(lat2) * math.cos(diffLong))

    initial_bearing = math.atan2(x, y)

    # Now we have the initial bearing but math.atan2 return values
    # from -180° to + 180° which is not what we want for a compass bearing
    # The solution is to normalize the initial bearing as shown below
    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360
    
    # azimuth is calculated assuming a small distance in relation to radius of Earth
    here = (source[0], source[1])
    plane = (dest[0], dest[1])
    
    distance = haversine(here,plane) * 1000
    altitude_diff = dest[2] - source[2]
    angular_drop = distance /(2*(6.371*1000000))
    elevation_angle = math.degrees(math.atan2(altitude_diff, distance) - angular_drop)

    
    print(compass_bearing)
    print(distance)
    print(angular_drop)
    print(elevation_angle)

    return compass_bearing, elevation_angle
    

# antennalocation Class
    #three properties lat, long, alitude 
