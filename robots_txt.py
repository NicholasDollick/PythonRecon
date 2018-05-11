import urllib2
import io

def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    req = urllib2.Request(path + "robots.txt", data = None)
    resp = urllib2.urlopen(req)
    data = resp.read()
    return data


