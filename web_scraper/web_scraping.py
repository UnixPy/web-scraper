from bs4 import BeautifulSoup


def scrape_web(source, parser):

    soup = BeautifulSoup(source, parser)

    price = soup.find('div', class_='product-price').meta.get('content')

    return price


