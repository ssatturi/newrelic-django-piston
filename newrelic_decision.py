import sys
try:
    import requests
    # We only have single newrelic license, so only use it on this IP...
    ip = requests.get('http://169.254.169.254/latest/meta-data/local-ipv4', timeout=3).text
    #ip = 'localhost'
    if ip == '10.0.2.13':
        print 'enable'
    else:
        print ''
except:
    print ''
