# coding:utf-8

import sys
import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
  
def getUrl(html):
    reg = r"(?<=a\shref=\"/watch).+?(?=\")"
    urlre = re.compile(reg)
    urllist = re.findall(urlre,html)
    format = "https://www.youtube.com/watch%s\n"
    for url in urllist:
        result = (format % url)
        print result,


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("%s	<query-words>" % sys.argv[0])
        print("parsed result is printed to line outupt")
        exit(1)
    query = sys.argv[1]

    pages = 10
    for i in range(1,pages):
        html = getHtml("https://www.youtube.com/results?search_query=" + query + "&lclk=short&filters=short&page=%s" % i)
        getUrl(html)
        i += 1

