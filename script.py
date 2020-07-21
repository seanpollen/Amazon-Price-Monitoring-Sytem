import requests
from bs4 import BeautifulSoup
import smtplib
import time

# Place the Amazon link for your desired product below. An instant camera is used as the example
URL = 'https://www.amazon.ca/Fujifilm-Instax-Mini-Instant-Camera/dp/B085282C1R/ref=sr_" \
      "1_5?dchild=1&keywords=camera&qid=1595343470&sr=8-5'

# Your user agent may be different. Update as needed
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/83.0.4103.116 Safari/537.36'}

# What price threshold would you like to be notified of?
desired_price = 90

# FILL THIS IN AS NEEDED
sending_email = ''
receiving_email = ''
sending_password = ''

# How many times a day would you like to check the price?
daily_checks = 2


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(id="priceblock_ourprice").getText()
    converted_price = float(price[5:7])

    if converted_price < desired_price:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(sending_email, sending_password)

    subject = 'There has been a price drop!! BUY NOW!'

    msg = f"Subject: {subject}\n\n{URL}"

    server.sendmail(
        sending_email,
        receiving_email,
        msg
    )

    print("message sent")


while True:
    check_price()
    time.sleep(86400 / daily_checks)
