#!/usr/bin/env python3

__title__ = 'Kilowattage'
__version__ = '0.1'
__license__ = 'BSD'
__desc__ = ('Calculates unknowns in utility pricing and usage.')
__url__ = 'https://github.com/cordella/Kilowattage'


import argparse

def parse_args():
    """ Set up, and return the results of, the argument parser. """
    parser = argparse.ArgumentParser(
        add_help=False, prog=__title__,
        usage='%(prog)s [options] [logging] network|ALL')

    optional = parser.add_argument_group(title='options')
    log = parser.add_argument_group(title='logging')

    optional.add_argument('-h', '--help', action='help',
                          help='print this help and exit')
    optional.add_argument('-v', '--version', action='version',
                          version='%(prog)s '+__version__,
                          help="show %(prog)s's version and exit")
#    optional.add_argument('-c', '--config', dest='config', default=None,
#                          help='specify an alternative configuration')
#    optional.add_argument('-d', '--daemon', dest='daemonise',
#                          action='store_true',
#                          help='start %(prog)s in daemon mode')
#    optional.add_argument('-p', '--pid', dest='pidfile', metavar='FILE',
#                          default=None, help='keep a pid file')

#    log.add_argument('-o', '--log', metavar='[FILE]', dest='logfile',
#                     default=None, help="log in FILE")
#    log.add_argument('-a', '--append', dest='logappend', action='store_true',
#                     help="append to FILE when logging")

#    parser.add_argument('network',
#                        help='an IRC network profile in your configuration')

    return parser.parse_args()

def separate_time(undivided_time, is_seconds = False):
    """ Given the time in hours or seconds, returns the time in common divisions,
        i.e. days, hours, minutes, seconds
    """
    if is_seconds is True:
        _undivided_time = undivided_time
    else:
        _undivided_time = undivided_time * 3600

    days, r1 = divmod(_undivided_time, 86400)  # 86400 s = 24 hr * 60 (min/hr) * 60 (s/min)
    hours, r2 = divmod(r1, 3600)  # 3600 s = 60 min * 60 (s/min)
    minutes, seconds = divmod(r2, 60)

    return int(days), int(hours), int(minutes), seconds


def calculate_time(cents_per_kWh, wattage, dollar_amount):
    """ Returns the time (in hours) that it would take to reach the monetary price (dollar_amount)
        given the cost of energy usage (cents_per_kWh) and power (wattage) of a device using that energy.
    """
    return 1 / (cents_per_kWh) * 1e5 * dollar_amount / wattage


if __name__ == '__main__':
    args = parse_args()

#    print(separate_time(3.034166666666666667))
    # [Out] (0, 3, 2, 3.0)
#    print(separate_time(calculate_time(4.271, 60, 1)))
    # [Out] (16, 6, 13, 43.22641067673885)

#    print("{:0.5g} {:s}".format((calculate_time(4.271, 60, 1)), 'hours'))
#    print("{0:d} days, {1:d} hours, {2:d} minutes, {3:f} seconds".format(separate_time(calculate_time(4.271, 60, 1))))
    print("{:d} days, {:d} hours, {:d} minutes, {:0.3f} seconds".format(*separate_time(calculate_time(4.271, 60, 1))))
