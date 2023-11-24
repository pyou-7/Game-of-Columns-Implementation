import urllib.request

BASE_URL = 'https://www.ics.uci.edu/~thornton/ics32a/ProjectGuide/FinalProject/Crawlspace/'

# crawl the url
def crawl(url: str) -> list:
    '''
    First, create a url_list which would contain a list of urls
    crawled by the given url. First, append the current url, then
    read the texts from the given url. If the text in the given
    url starts with LINK, new url will be created by adding the
    BASE_URL to the new extension, then extend the recursion to
    the url_list. At the base condition, return the url_list which
    contains all the the url crawled by the function.
    '''
    url_list = []
    url_list.append(url)
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read()
    text = data.decode(encoding = 'utf-8')
    lines = text.splitlines()
    for line in lines:
        if line.startswith('LINK'):
            url = BASE_URL + line[5:]
            url_list.extend(crawl(url))
        else:
            pass
    return url_list
        
                
                
