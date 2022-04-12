from bs4 import BeautifulSoup
import requests
import smtplib

my_email = ""
password = ""

url = "https://www.amazon.es/dp/B07RHPSCGS?ref_=cm_sw_r_cp_ud_dp_HJBN9ZW8S4QGF24BVTJZ"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Accept-Language": "es-ES"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
price = soup.find_all("span", class_="_p13n-desktop-sims-fbt_price_p13n-sc-price__bCZQt")
final_price = price[0].getText().split()[0].split(",")[0]+"."+price[0].getText().split()[0].split(",")[1]

f_price = float(final_price)

title = soup.find(id="productTitle").getText().strip()
tittle = title.split(" Impermeable ")[0]

idealPrice = 35

if f_price < idealPrice:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="rr.david.marlor@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message.encode('utf-8')}\n{url}"
        )
