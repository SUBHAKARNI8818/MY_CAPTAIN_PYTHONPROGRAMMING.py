import requests
from bs4 import Beautifulsoup
import pandas
import argparse
import connect

parser = argparse.arugumentparser()
parser.add_argument("--page_num_max", help="Enter the number of pages to parse ", type = int)
parser.add_argument("--dbname", help="Enter the number of pages to parse ", type = int)
args = parser.parse_args()

oyo_url = "https://www.oyorooms.com/hotels-in-bamgalore/?pages="
page_num_Max = args.page_num_max
scraped_info_list=[]
connect.connect(args.dbname)

for page_num in range(1, page_num_Max):
    req = requests.get(oyo_url + str(page_num))
    content = req.content
    soup = Beautifulsoup(content,"html.parser")
    all_hotels = soup.find_all("div", {"class": "hotelcardlisting"})
    
    for hotels in all_hotels:
        hostel_dict = {}
        hotel_dict["name"]=hotel.find("h3", {"class": "listingHotelDescription_hotelname"}).text
        hotel_dict["address"]=hotel.find("span",{"itemprop": "streetAddress"}).text
        hotel_dict["price"]=hotel.find("span",{"class": "listingprice_finalprice"}).text
        
        try:
        
            hotel_dict["rating"]=hotel.find("span",{"class" : "hotelRating_ratingsummary"}).text
            
        except ArrtributeError :
             pass
             
        parse_amentities_element = hotel.find("div",{"class": "amenitywrapper"})
        amenitie_list=[]
        
        for amenity in parent_amentities_element.find_all("div",{"class": "amenitywrapper_amenity"}):
             amenitie_list.append(amenity.find("span",{"class": "d-body-sm"}).text.strip())
        hotel_dict["amenities"]=','.join(amenities_list[:-1])
        scraped_info_list.append(hotel_dict)
        
dataFrame = pandas.DataFrame(scraped_info_list)
dataFrame.tp_csv("Oyo.csv")

# connect
import sqlite3
def connect(dbname):
    conn= sqlite3.connect(dbnmae)
    conn.execute("CREATE TABLE IF NOT EXISTS OYO_HOTELS (NAME TEXT, ADDRESS TEXT, PRICE INT, AMENITIES TEXT, RATING TEXT)")
    print("Table created succcessfully!")
    conn.close()
    
def insert_into_table(dbname, values):
    conn=sqlite3.connect(dbname)
    inser_sql = "INSERT INTO OYO_HOTELS (NAME, ADDRESS, PRICE, AMENITIES, RATING) VALUES(?,?,?,?)"
    conn.execute(insert_sql, values)
    conn.commit()
    conn.close()
    
def get_hotel_info(dbname):
    conn=sqlite3.connect(dbname)
    cur=conn.cursor()
    cur.execute("SELECT * OYO_HOTELS")
    table_data = cur.fetchall()
    for record in table_data:
        print(record)  
