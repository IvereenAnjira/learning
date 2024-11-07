# import libaries 
from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib

# connect to website,Computer,requst page, get HTML code,print HTML code all respactivly 
URL="https://www.jumia.com.ng/realme-c51-6.74-4gb-ram128gb-rom-android-13-black-272069102.html"
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
page= requests.get(URL, "lxml")
soup1= BeautifulSoup(page.content,'html.parser')
soup2= BeautifulSoup(soup1.prettify(),'html.parser')
print(soup2)

#get Name
#Price
#Rating
#Number of reviews
Product_title= soup2.find(class_='-fs20 -pts -pbxs').get_text()
Price= soup2.find(class_='-b -ubpt -tal -fs24 -prxs').get_text()
Rating= soup2.find(class_='stars _m _al').get_text()
Number_of_reviews=soup2.find(class_='-plxs _more').get_text()

Product_title=Product_title.strip()
Price=Price.strip()[2:]
Rating=Rating.strip()
Number_of_reviews=Number_of_reviews.strip()[1:19]

print(Product_title)
print(Price)
print(Rating)
print(Number_of_reviews)

# Get date and time 
date=datetime.date.today()
time_= datetime.datetime.now()
#print(time_.time())
time_=time_.strftime("%H:%M:%S")
print(time_)
print(date)

#create csv
import csv
header=['Product_title','Price','Rating','Number_of_reviews','date','time_']
Data=[Product_title,Price,Rating,Number_of_reviews,date,time_]

with open('amazon webscraping.csv','w',newline='',encoding='UTF8') as f:
    writer=csv.writer(f)
    writer.writerow(header)
    writer.writerow(Data)

#automating to check price at a set time 
def check_price():
    URL="https://www.jumia.com.ng/realme-c51-6.74-4gb-ram128gb-rom-android-13-black-272069102.html"
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
    page= requests.get(URL, "lxml")
    soup1= BeautifulSoup(page.content,'html.parser')
    soup2= BeautifulSoup(soup1.prettify(),'html.parser')

    Product_title= soup2.find(class_='-fs20 -pts -pbxs').get_text()
    Price= soup2.find(class_='-b -ubpt -tal -fs24 -prxs').get_text()
    Rating= soup2.find(class_='stars _m _al').get_text()
    Number_of_reviews=soup2.find(class_='-plxs _more').get_text()
    
    Product_title=Product_title.strip()
    Price=Price.strip()[2:]
    Rating=Rating.strip()
    Number_of_reviews=Number_of_reviews.strip()[1:19]
    date=datetime.date.today()
    time_= datetime.datetime.now()
    time_=time_.strftime("%H:%M:%S")

    import csv
    header=['Product_title','Price','Rating','Number_of_reviews','date','time_']
    Data=[Product_title,Price,Rating,Number_of_reviews,date,time_]

    with open('amazon webscraping.csv','a+',newline='',encoding='UTF8') as f:
        writer=csv.writer(f)
        writer.writerow(Data)

while(True):
    check_price()
    time.sleep(5)

