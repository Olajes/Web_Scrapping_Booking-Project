# this app scrap data from booking.com
from bs4 import BeautifulSoup
import csv
import requests
import lxml
import time
import random


"""
Give the url, file name
Greeting
Start Scrapping
hotel_name,
price
location
ratings
reviews
link
save the file in csv

"""


#url_text = 'https://www.booking.com/searchresults.en-gb.html?ss=India&ssne=India&ssne_untouched=India&efdco=1&label=in-paLo9N5HEQwFUOiXFghN8QS379606794439%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-303403359744%3Alp21554%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YfqnDqqG8nt10AsofPfvtt0&sid=991d150dbbb466b92725fa2dce6b8c2e&aid=1610684&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=98&dest_type=country&checkin=2025-05-01&checkout=2025-05-02&group_adults=2&no_rooms=1&group_children=0'
mumbai = "https://www.booking.com/searchresults.en-gb.html?ss=Mumbia&ssne=India&ssne_untouched=India&label=in-paLo9N5HEQwFUOiXFghN8QS379606794439%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-303403359744%3Alp21554%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YfqnDqqG8nt10AsofPfvtt0&sid=991d150dbbb466b92725fa2dce6b8c2e&aid=1610684&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=-2092174&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=72b269d6e018012a&ac_meta=GhA3MmIyNjlkNmUwMTgwMTJhIAAoATICZW46Bk11bWJpYUABSgZtdW1iYWlQmSc%3D&checkin=2025-05-01&checkout=2025-05-02&group_adults=2&no_rooms=1&group_children=0"


def web_scrapper2(web_url, file_name):

    # greetings
    print("Thanks you sharing the url and file name!\n❤\nReading the content!")
    
    num = random.randint(3,7)



    # processing
    time.sleep(num)

    
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'}



    response = requests.get(web_url, headers=header)

    if response.status_code==200:
        print("Connected to the website")
        
        html_content = response.text
        
        # creating soup

        soup = BeautifulSoup(html_content,'lxml')


        #print(soup.prettify())

    # main container
        hotel_divs = soup.find_all('div', role= "listitem")

        with open(f'{file_name}.csv', 'w',newline='', encoding='utf-8') as file_csv:
            writer= csv.writer(file_csv)

            # adding Header

            writer.writerow(['hotel_name','location','price','rating','score','review','link'])

        # 
            for hotel in hotel_divs:
                hotel_name = hotel.find('div', class_= "f6431b446c a15b38c233").text.strip()
                hotel_name if hotel_name else "NA"
                
                location = hotel.find('span', class_= "aee5343fdb def9bc142a").text.strip()
                location if location else "NA"
                
                price = hotel.find('span', class_="f6431b446c fbfd7c1165 e84eb96b1f").text.replace('NGN','')
                price if price else "NA"
                
                rating = hotel.find('div', class_ = "a3b8729ab1 e6208ee469 cb2cbb3ccb").text.strip()
                rating if rating else "NA"
                
                score = hotel.find('div', class_="a3b8729ab1 d86cee9b25").text.strip().split(' ')[-1]
                score if score else "NA"
                
                review = hotel.find('div', class_="abf093bdfe f45d8e4c32 d935416c47").text.strip()
                review if review else "NA"

                #getting link
                link = hotel.find('a', href= True).get('href')
                link if link else "NA"


                # saving the file into csv

                writer.writerow([hotel_name,location,price,rating,score,review,link])


                #print(hotel_name)
                #print(location)
                #print(price)
                #print(rating)
                #print(score)
                #print(review)
                #print(link)
                #print('')


    else:
                print(f"Connection Failed!{response.status_code}") 


# if using this script directly then below task will be executed

if __name__ == '__main__':
      url = input("Please enter url!:")
      fn = input("Please give file name! :")

      # calling the function

      web_scrapper2(url,fn)