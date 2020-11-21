import gmail_stuff as gmail
import web_scraping as web
from time import sleep
import requests
import datetime
import os


web_link = requests.get('https://www.komplett.no/product/1168752/datautstyr/pc-komponenter/skjermkort/asus-geforce-rtx-3070-dual').text
price = web.scrape_web(source=web_link, parser='html.parser')

# Gmail variable things
today = datetime.date.today()

sender = "flovildmidtlielinus@gmail.com"
reciever = "kjetil@flovild-midtlie.name"

token = os.environ.get('GMAIL_APP_CODE') # password for gmail account

subject = "Web Scraper Status!"
price_lower = f"This message was sent using an automated python module. The date of which this gmail was sent is {today}. The price of the rtx 3070 is: {price} The price of the rtx 3070 has dropped since the last gmail! If the rtx 3070 is still on sale the next day, another gmail will be recieved.\n\nsincerely WEB_BOT()"

price_same = f"This message was sent using an automated python module. The date of which this gmail was sent is {today}. The current price of the rtx 3070 is: {price} The price has not changed since last gmail.\n\nIf the price of the rtx 3070 stays the same until monday, another gmail will be recieved.\n\nsincerely WEB_BOT()"

while True:
    # Scrapes website for price
    web_link = requests.get('https://www.komplett.no/product/1168752/datautstyr/pc-komponenter/skjermkort/asus-geforce-rtx-3070-dual').text
    price = web.scrape_web(source=web_link, parser='html.parser')

    price = float(price)

    print(price)

    if price < 6390.0:
        gmail.send_gmail(sender, reciever, token, subject, price_lower)
        sleep(86400)
    elif price == 6390.0  and datetime.date.today().weekday() == 0:
        gmail.send_gmail(sender, reciever, token, subject, price_same)
        sleep(86400)
    else:
        sleep(3600)

