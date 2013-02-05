#!/usr/bin/env python
# encoding: utf-8


def clean_number(number):
    import re
    number = re.sub(' +', '', number)
    number = re.sub('[^\d.]+', '', number)
    numr = re.compile("^(\+)?(\d+)$")
    m = numr.match(number)
    if m:
        pls, number = m.groups()
        if pls:
            pls = '00'
        else:
            #use US std
            pls = '001'
        return pls + number


def dial_with_snom(host, username, pwd, number):
    import urllib2
    import base64

    auth_encoded = base64.encodestring('%s:%s' % (username, pwd))[:-1]

    url = 'http://%s/command.html?number=%s' % (host, number)

    req = urllib2.Request(url)
    req.add_header('Authorization', 'Basic %s' % auth_encoded)
    try:
        urllib2.urlopen(req)
    except:
        pass


def main():
    import sys
    from optparse import OptionParser

    usage = 'usage: %prog [options] user -h for help'
    parser = OptionParser(usage)
    parser.add_option('-d', '--host', action='store',
    type='string', dest='host', help='host ip')
    parser.add_option('-u', '--user', action='store',
    type='string', dest='user', help='user name')
    parser.add_option('-p', '--pwd', action='store',
    type='string', dest='pwd', help='password')
    parser.add_option('-n', '--number', action='store',
    type='string', dest='number', help='number to dial')

    (options, args) = parser.parse_args()
    if options.host and options.user and options.pwd and options.number:
        dial_with_snom(options.host, options.user, options.pwd,
                       clean_number(options.number))
    else:
        parser.print_help()

if __name__ == '__main__':
    import sys
    status = main()
    sys.exit(status)
