import urllib2
from bs4 import BeautifulSoup


def get_html(url):
    request_html = urllib2.Request(url)
    try:
        response = urllib2.urlopen(request_html)
        html = response.read()
    except Exception, e:
        return None
    return html


def get_links(url):
    html = get_html(url)
    result = []
    if not html:
        return result
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all('a')
    for link in links:
        href = link.attrs['href']
        if not href in result:
            result.append(href)
    return result


for link in get_links('https://github.com'):
    print link
