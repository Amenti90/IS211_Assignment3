"""
1. Download file from web.
2. Process file using csv module.
3. Use regex to tally image file types and then display percentage: type/total.
4. Browser/ Total
5. Display top browser.
6. EXTRA: Total number of hits sorted by hour of the day. Second column has datetime record which can be manipulated to extract the '
hour using the datetime module.

Dive into Python  Chapter 6 & 7
"""

import  urllib2
from bs4 import BeautifulSoup


TEST_URL = "http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv"


def downloadData(url):
    file= urllib2.urlopen(url)
    return file 



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="Add URL", action="store", type=str, required=True)
    parser.add_argument("--name")
    args = parser.parse_args()

    print("URL passed = {}".format(args.url))
    page = downloadData(args.url)



