from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import csv

browser = webdriver.Chrome("chromedriver.exe")
start = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser.get(start)
time.sleep(10)

def scrap():
    header = ['Name','Distance','Mass','Radius']
    sun = []

    time.sleep(1)
    soup = BeautifulSoup(browser.page_source,'html.parser')
    star_table = soup.find('table')
    for tr_tag in star_table.find_all("tr"):
        td_tags = tr_tag.find_all("td")
        temp_list = []
        for index , td_tag in enumerate(td_tags):
            temp_list.append(td_tag.contents[0])
    
    sun.append(temp_list)
    
    with open("suns.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(header)
        csvwriter.writerows(sun)

scrap()