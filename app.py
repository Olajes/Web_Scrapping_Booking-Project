# This app scrap products data from amazon website

# BeautifulSoup4
# requests
# lxml


from bs4 import BeautifulSoup
import requests
import csv


url = "https://www.amazon.in/Apple-Headphones-Cancellation-Transparency-Personalised/dp/B0DGJ61KZ8/ref=sr_1_4?crid=2809TN084SOHQ&dib=eyJ2IjoiMSJ9.M94QDtrjaJjxlFaXNPyoIy-ihZmoL0FXSVht8PMtNh_wq_61UBe2teuWVV92yCsvruZUKUWg-gPAAkWbsJWSa9WTnUa65iA7hdk_O5KLIakkB72iGJ87OKVe0xpXLz4tIUqlUmoSEmeWOsprGDIGGOg2LI615At3x2E0H7Fy0BNAmhL-XWDfdertMPpFhp-w2ggT5owxQoJrr-DPFJewcVS1PoeOu1bGCXvTlTSLU0c.aBaPHQq6yuaPZfovrQ42326ma6pTVM31EBGCQkhSZXA&dib_tag=se&keywords=apple%2Bairpods%2Bpromax&nsdOptOutParam=true&qid=1744800843&sprefix=%2Caps%2C657&sr=8-4&th=1"

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}


response = requests.get(url, headers=headers)

if response.status_code ==200:
    # print(response.status_code)
    html_content = response.text
else:
    print("fetching error", response.status_code)


print(html_content)



soup = BeautifulSoup(html_content, 'lxml')

# print(soup.prettify())

product_title = soup.find( "span",id ="productTitle").text.strip()

product_price= soup.find( "span", class_= "a-price-whole").text.strip()

product_rating = soup.find("span", id= "acrPopover").text.strip()

product_bp = soup.find("ul", class_ = "a-unordered-list a-vertical a-spacing-mini").text.strip()
product_description = soup.find("div", id="productDescription").text.strip()
reviews = soup.find("ul", id= "cm-cr-dp-review-list").text.strip()







# saving the data

with open("amazon_airpod_pro_max.csv", mode='w', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["product_title","product_price","product_rating","product_bp","product_description","reviews"])

    writer.writerow([product_title,product_price,product_rating,product_bp,product_description,reviews])


print("data saved!")

