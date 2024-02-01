import requests
from bs4 import BeautifulSoup as bs

HEADERS = ({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Alt-Used': 'www.amazon.com',
    'Connection': 'keep-alive',
    'Cookie': 'AMCV_7742037254C95E840A4C98A6%40AdobeOrg=1585540135%7CMCIDTS%7C19745%7CMCMID%7C69698505563784285960651308774267527481%7CMCAAMLH-1706497600%7C3%7CMCAAMB-1706497600%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1705900000s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19749%7CvVersion%7C4.4.0; regStatus=pre-register; aws-target-visitor-id=1705892799951-519820.48_0; aws-target-data=%7B%22support%22%3A%221%22%7D; session-id=134-8475813-5782246; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:HK"; csm-hit=tb:s-9MTMWMRP96SRPCKZ2RMT|1706752748888&t:1706752750965&adb:adblk_yes; ubid-main=130-6651553-9159959; session-token=khX61OGqfxOCv/lldRMIKzlpQmti/h660jNv/3I05xmPRKQX+4VqNX1/1OAOWBt8UwTb0FMAa/8USjs/Iy0NuyRNvhzSHyqyHAqiSNSU9MS8Jc4sy/lBs+ruSBAepwf5HBBpW9CdYI+hXw/qqaRHPj/KDaZJDOjZGET5T0Oyw8V39NhCxsskk1j6SBLpzsZjghjiXW4W8HNxLDzapZZLzFUC8Ee5L4DFZS0ol1Kury0I7JVI9+6l8t1py5JjsZfcsaZ9tFlmfsWh3qbB1rskTo7yhLUr3z83CZazy5xP3E1xnkqp8gFFlmKZf0Eg9Tbmj8Ki9gFoupdWj2FpVAUn78nM4IiEZmTuzwLhM799/C421Y3WUGB+xrWiAlC5eT0N; lc-main=en_US; x-main="8guDb1MlVF0NmV4REzPYVsJ1gm6lO4yNwKbW1yqBGgDZuxGHSbrkFE2TH3LM@plJ"; at-main=Atza|IwEBIF7kVuB1Vf_evWalYtz2dGA47A-p91JRB3xJy93RKL2vVwGE9aGw2cKK6VOhcdpFdDYvXIRv_Xg33C-p3a2r3YWfMLP9GpXWVQtw3qNiSdwlJJUBQO_fXjRVq4gwgrjCDa9COTbIdK-TKq2rt-v7bitcjNRXteXfeQIG64LJeYh-J4VhRt34I8xgR4_ukNIbpCKx3lYOIm8aMA41-YeZKNa20pyxgwC03KGDZxN4VagNSA; sess-at-main="RHskkpTdyO+NouZXyFtbvxx9uPo1mTNygKfjytZFDD0="; sst-main=Sst1|PQE-6ALOq_BMV4ykQDMdytQnCV1aLJvD3KqnMOE7XkMe7Eg0i9VYsQCDvLAwlsJROBqIRc7jeWy6BzIqMIQqukRsnM9p2Ju49qlWPLBC4D8TR6SITkWypqRJwM41Bk5Gg2EGHgdveeO2drN0vP4JIQcxXDdFXZ70a51AhO_5HiuCyT2PZS4ZJ6SdQBhcvKXkSsQFJwnOw2ikJqtL75VRvxVMOtouEYe6Tq8nI7Uq4QsQOE3HpaKaulkLe18K2qUDqf0IszPpQ5uYoxLw-ds7P-NDQAAror1ydNo5guJzSretN-8; skin=noskin',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'TE': 'trailers'
})
url = "https://www.amazon.com/AMD-4500-12-Thread-Unlocked-Processor/product-reviews/B09VCJN7HZ/ref=cm_cr_arp_d_paging_btm_prev_1?ie=UTF8&pageNumber=1&reviewerType=all_reviews"
comment_urls = []

def getData(url, headers):
    r = requests.get(url, headers=headers)
    resp = r.content
    soup = bs(resp, 'html.parser')
    return soup

def getNextPage(soup):
    if not soup.find('div', class_ = 'a-text-center celwidget a-text-base aok-float-left cr-pagination-medium-right-padding').find('ul', class_ = 'a-pagination').find('li', class_ = 'a-disabled a-last'):
        page = soup.find('div', class_ = 'a-text-center celwidget a-text-base aok-float-left cr-pagination-medium-right-padding').find('ul', class_ = 'a-pagination').find('li', class_ = 'a-last').find('a').get('href')
        next_url = "https://www.amazon.com" + page
        return next_url
    else:
        return  

def getReviews(url, headers):
    soup = getData(url, headers)
    comments = soup.find('div', class_ = 'a-section a-spacing-none review-views celwidget').find('div', class_ = 'a-row a-spacing-none').find('span', class_ = 'a-size-base review-text review-text-content').find('span').get_text()
    return comments

while True:
    soup = getData(url, HEADERS)
    url = getNextPage(soup)
    if str(url) != "None":
        comment_urls.append(url)
    if not url:
        break

for url in comment_urls:
    comments = getReviews(url, HEADERS)
    with open('./comments.md', 'a') as f:
        f.writelines(comments)
        f.writelines('\n')
    f.close()

