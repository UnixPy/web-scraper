from bs4 import BeautifulSoup


def scrape_web(source, parser):

    soup = BeautifulSoup(source, parser)

    price = soup.find('meta', itemprop='price')
    price = int(price['content'].split('.')[0])

    return price