# -*- coding: utf-8 -*-

import click
from .__version__ import __version__
from .maat import Args, calculate_azimuth_elevation

@click.command()
@click.argument('ip')
@click.option('--loc', nargs=3, type=float, help='Groundstation coordinates (signed deg) lat, long, altitude (meters)')
@click.option('--system', type=int, help='System ID [1-255]')
@click.option('--component', type=int, help='Component ID [1-255]')
def main(ip, loc, system, component):
    #import pdb; pdb.set_trace()
    args = Args(ip, loc, system, component)
    test_dest = 40.003730, -105.258362, 1000
    calculate_azimuth_elevation(args.loc, test_dest)
    # setup mavlink mavfile (UDP)
    # Give system, component, IP connecting, port connecting to
    # hand mavfile to mavconn constructor
    # add_timer(heartbeat) heartbeat function ^
    # Use closures to register 2 handles for global
    #stay in context manager until signal.interrupt


if __name__ == '__main__':
    main()
