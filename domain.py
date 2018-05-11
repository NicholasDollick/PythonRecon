from tld import get_tld

#get top level domain from passed url
def get_domain_name(url):
    domain_name = get_tld(url)
    return domain_name

