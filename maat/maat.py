import click
from mavconn import MAVLinkConnection


@click.command()
@click.argument('ip')
@click.option('--loc', nargs=3, type=float, help='Groundstation coordinates (signed deg) lat, long, altitude (meters)')
@click.option('--system', type=int, help='System ID [1-255]')
@click.option('--component', type=int, help='Component ID [1-255]')
class Args:

    def __init__(self, ip, loc, system, component):
        ip_addr_port = ip.split(':')
        self.ip_addr= ip_addr_port[0]
        self.ip_port= ip_addr_port[1]
        self.lat=loc[0]
        self.long=loc[1]
        self.altitude=loc[2]
        self.mavsystem = system
        self.mavcomponent = component
        print(self.ip_addr)
        print(self.ip_port)
        print(self.lat)
        print(self.long)
        print(self.altitude)
        print(self.mavsystem)
        print(self.mavcomponent)


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
    pass


def calculate_azimuth_elevation(source, dest):
    #inputs are two triples (tuples) with lat, long, altitude
    #return azimuth and elevation from source to dest
    pass


def main():
    args = Args()
    # parse command line arguments
    # setup mavlink mavfile (UDP)
        # Give system, component, IP connecting, port connecting to
    # hand mavfile to mavconn constructor
    # add_timer(heartbeat) heartbeat function ^
    # Use closures to register 2 handles for global
    
if __name__ == '__main__':
    main()
    

# antennalocation Class
    #three properties lat, long, alitude 
