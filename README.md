# Web_Scrapping_Booking.com-Project

## 📌 Project Overview

This project is a web scraping application designed to extract hotel details from [Booking.com](https://www.booking.com). It scrapes hotel information such as:

- 🏨 Hotel Name  
- 💰 Price  
- 📍 Location  
- ⭐ Rating  
- 📝 Review Count  
- 🔗 Booking Link  

The data is saved as a CSV file in the local directory, based on user input.

## 🎯 Objectives

- **Automate Hotel Data Collection** – Efficiently extract key hotel details from Booking.com.
- **Flexible Scraping** – Allow users to input a custom Booking.com search URL and output file name.
- **Data Storage** – Save the data in a clean, structured CSV format.
- **Error Handling & Performance** – Implement request headers and random sleep timers to avoid bot detection.
- **User-Friendly Execution** – Seamless command-line experience with minimal setup.

## 🔧 Technologies & Libraries Used

- **Python 3.x**
- **BeautifulSoup4** – For HTML parsing and detail extraction.
- **Requests** – To handle HTTP requests.
- **CSV** – For saving the scraped data.
- **LXML** – Fast and efficient HTML parser.

---

## 📂 Features & Workflow

1. **User Input**:
   - Booking.com search URL
   - Desired output CSV filename

2. **Scraper Execution**:
   - Fetches the specified page
   - Extracts:
     - 🏨 Hotel Name
     - 💰 Price
     - 📍 Location
     - ⭐ Rating
     - 📝 Number of Reviews
     - 🔗 Booking Link

3. **Data Output**:
   - Saves the extracted hotel data into a CSV file in the local directory

4. **Performance Optimization**:
   - Random sleep intervals between requests to mimic human browsing behavior
