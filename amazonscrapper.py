import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = "https://www.amazon.ca/Apple-MMEF2AM-AirPods-Wireless-Bluetooth/dp/B01MQWUXZS/ref=sr_1_3?keywords=airpods&qid=1562649710&s=gateway&sr=8-3";

headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'}

def check_price():
    page = requests.get(url, headers=headers);

    soup = BeautifulSoup(page.content, 'html.parser');

    title = soup.find(id="productTitle").get_text();

    price = soup.find(id="priceblock_ourprice").get_text();
    converted_price = float(price[5:11])

    if (converted_price < 200):
        send_mail();

    print(converted_price)
    print (title.strip())



def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587);
    server.ehlo();
    server.starttls()
    server.ehlo()

    server.login("sameplemail@hotmail.com", 'password123');

    subject = "The Price Fell!!";
    body = "Click this link for your deal! https://www.amazon.ca/Apple-MMEF2AM-AirPods-Wireless-Bluetooth/dp/B01MQWUXZS/ref=sr_1_3?keywords=airpods&qid=1562649710&s=gateway&sr=8-3";


    msg = (f'Subject: {subject}\n\n{body}');


    server.sendmail(
        'sampleemail@hotmail.com',
        'toemail@hotmail.com',
        msg
    )

    print("EMAIL WAS SENT")
    server.quit()



def main():
    while(True):
        check_price();
        time.sleep(60*60);
        


if __name__ == '__main__':
    main();
