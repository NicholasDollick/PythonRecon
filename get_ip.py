import os

def get_ip(url):
    cmd = "host " + url
    process = os.popen(cmd)
    ip = str(process.read()).split()[3]
    return ip
