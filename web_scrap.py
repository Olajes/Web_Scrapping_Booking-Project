# This app do webscrap data from html

from bs4 import BeautifulSoup
import csv


#html_path = "C:/Users/user/Desktop/STEVE CATALOG/PYTHON TUTORIAL/PYTHON_DATA_PROJECT/4_Web_Scraping/apple_store.html"


html_path = r"C:\Users\user\Desktop\STEVE CATALOG\PYTHON TUTORIAL\PYTHON_DATA_PROJECT\4_Web_Scraping\apple_store.html"

with open(html_path, "r", encoding="utf-8") as html_file:
    html_content = html_file.read()



#print(html_content)

soup = BeautifulSoup(html_content, 'html.parser')


header = soup.find('h1').text

menus = soup.find_all('a')
for menu in menus:
    print(menu.text)

products_divs = soup.find_all('div', class_ = "product")

# opening csv file to store the data

with open("apple_products.csv", 'w',encoding="utf-8") as file_csv:
    writer = csv.writer(file_csv)


# adding header
    writer.writerow(['product_name','price','qty_left','rating','est'])



    for product in products_divs:
        product_name = product.find('h3').text  #if product.find('h3').text else 'NA'
        price = product.find('p').text.replace('Price: ', '')
        qty_left = product.find_all('p')[1].text.replace('Quantity Available ', '')
        rating = product.find('p', class_ ="rating").text
        est= product.find_all('p')[-1].text.replace('Estimated Shipping: ', '')



        
        # saving the rows

        writer.writerow([product_name,price,qty_left,rating,est])


print("Congratulations data scrapped and saved successfully")


