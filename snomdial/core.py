import phonenumbers


def normalize_number(number, ccode):
    m = phonenumbers.parse(number, ccode)
    return "00%s%s" % (m.country_code, m.national_number)


def dial_with_snom(host, username, pwd, number, ccode):
    import urllib2
    import base64

    auth_encoded = base64.encodestring('%s:%s' % (username, pwd))[:-1]
    number = normalize_number(number, ccode)

    url = 'http://%s/command.html?number=%s' % (host, number)

    req = urllib2.Request(url)
    req.add_header('Authorization', 'Basic %s' % auth_encoded)
    try:
        urllib2.urlopen(req)
    except:
        pass
