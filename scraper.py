from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers = ["V_Mag", "Proper_name", "Bayer_designation", "Distance", "Spectral class", "Mass", "Radius", "Luminosity"]
    planet_data = []
    
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for th_tag in soup.find_all("th", attrs={"class", "exoplanet"}):
        tr_tags = th_tag.find_all("")
        temp_list = []
        for index, tr_tag in enumerate(tr_tags):
            if index == 0:
                temp_list.append(tr_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(tr_tag.contents[0])
                except:
                    temp_list.append("")
        planet_data.append(temp_list)
        #browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()