import click
#from mavconn import MAVLinkConnection, Timer


@click.command()
@click.argument('ip')
@click.option('--loc', nargs=3, type=float, help='Groundstation coordinates (signed deg) lat, long, altitude (meters)')
@click.option('--mavaddress', nargs=2, type=int, help='System and component address [1-255],[1-225]')
class maat:

    def __init__(self, ip, loc, mavaddress):
        self.ip=ip
        self.loc=loc
        self.mavaddr = mavaddress
        print(self.ip)
        print(self.loc)
        print(self.mavaddr)

if __name__ == '__main__':
    maat()
