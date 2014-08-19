#!/usr/bin/env python
# encoding: utf-8

from snomdial import dial_with_snom


def main():
    from optparse import OptionParser

    usage = 'usage: %prog [options] user -h for help'
    parser = OptionParser(usage)
    parser.add_option('-H', '--host', action='store',
                      type='string', dest='host', help='host ip')
    parser.add_option('-u', '--user', action='store',
                      type='string', dest='user', help='user name')
    parser.add_option('-p', '--pwd', action='store',
                      type='string', dest='pwd', help='password')
    parser.add_option('-n', '--number', action='store',
                      type='string', dest='number', help='number to dial')
    parser.add_option('-c', '--country', action='store',
                      type='string', dest='ccode', help='country code',
                      default='US')

    (options, args) = parser.parse_args()
    if options.host and options.user and options.pwd and options.number:
        dial_with_snom(options.host, options.user, options.pwd,
                       options.number, options.ccode)
    else:
        parser.print_help()

if __name__ == '__main__':
    import sys
    status = main()
    sys.exit(status)
