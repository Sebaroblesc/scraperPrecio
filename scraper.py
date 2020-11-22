import requests
from bs4 import BeautifulSoup
import smtplib
from re import sub
from decimal import Decimal
import time



URL = 'https://www.divinatechnology.cl/ipad-102-32gb-octava-generacion'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    titulo = soup.find('h1', 'page-header').get_text()
    precio = soup.find(id="product-form-price").get_text()

    converted_precio = Decimal(sub(r'[^\d.]', '', precio))

    if(converted_precio < 320.000):
        send_mail()

    print(titulo)
    print(converted_precio)

    if(converted_precio > 320.000):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('sebaroblestest@gmail.com', 'Seba6578008@')

    subject = 'Bajo de precio!'
    body = 'Revisa en el link: https://www.divinatechnology.cl/ipad-102-32gb-octava-generacion'

    msg = f"Subject: {subject}\n\n{body}"

    reciben = 'Zero.soad@gmail.com,sebaroblesca@gmail.com'
    server.sendmail(
        'sebaroblestest@gmail.com',
        reciben.split(','),
        msg
    )
    print('EMAIL ENVIADO.')
    server.quit()

while(True):
    check_price()
    time.sleep(60 * 60)