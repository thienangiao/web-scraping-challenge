
import pandas as pd
import requests
import time

from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from splinter.exceptions import ElementDoesNotExist
from pprint import pprint

def scrape_info():

    # NASA Mars News
    # Latest news URL
    news_url = 'https://mars.nasa.gov/news'
    # Retrieve page with the requests module
    response = requests.get(news_url)
    # Create BeautifulSoup object; parse with 'lxml'
    news_soup = BeautifulSoup(response.text, 'lxml')
    # Retrieve the latest news title
    news_title = news_soup.find('div', class_='content_title').text.strip()
    # Retrieve the latest news paragraph text
    news_p = news_soup.find('div', class_='rollover_description_inner').text.strip()


    # JPL Mars Space Images
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    # Website url
    img_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(img_url)
    time.sleep(1)
    # Scrape page into Soup
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')
    # Retrieve element that contain featured image
    featured_image = img_soup.find('img', class_='headerimage fade-in')['src']
    # Image url
    featured_image_url = img_url[:56]+featured_image


    # Mars Facts
    # Website url
    facts_url = 'https://space-facts.com/mars'
    # Use Panda's `read_html` to parse the url
    tables = pd.read_html(facts_url)
    # Input table to dataframe
    df=tables[0]
    # Convert table data to html
    html_table = df.to_html(header=False,index=False)


    # Mars Hemispheres
    # Cerberus Enhanced URL
    cerb_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    cerb_response = requests.get(cerb_url)
    cerb_soup = BeautifulSoup(cerb_response.text, 'lxml')
    # Retrieve image and create image url
    cerb_img = cerb_soup.find('img', class_='wide-image')['src']
    cerb_img_url = cerb_url[:29]+cerb_img


    # Schiaparelli Enhanced URL
    schi_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    schi_response = requests.get(schi_url)
    schi_soup = BeautifulSoup(schi_response.text, 'lxml')
    # Retrieve image and create image url
    schi_img = schi_soup.find('img', class_='wide-image')['src']
    schi_img_url = schi_url[:29]+schi_img

    # Syrtis Major Enhanced URL
    syrt_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    syrt_response = requests.get(syrt_url)
    syrt_soup = BeautifulSoup(syrt_response.text, 'lxml')
    # Retrieve image and create image url
    syrt_img = syrt_soup.find('img', class_='wide-image')['src']
    syrt_img_url = syrt_url[:29]+syrt_img


    # Valles Marineris Enhanced URL
    vall_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    vall_response = requests.get(vall_url)
    vall_soup = BeautifulSoup(vall_response.text, 'lxml')
    # Retrieve image and create image url
    vall_img = vall_soup.find('img', class_='wide-image')['src']
    vall_img_url = vall_url[:29]+vall_img

    # Store data in a dictionary
    mars_data = {
                "vall_title": "Valles Marineris Hemisphere",
                "vall_img_url": vall_img_url,
                "cerb_title": "Cerberus Hemisphere",
                "cerb_img_url": cerb_img_url,
                "schi_title": "Schiaparelli Hemisphere",
                "schi_img_url": schi_img_url,
                "syrt_title": "Syrtis Major Hemisphere",
                "syrt_img_url": syrt_img_url,
                "news_title": news_title,
                "news_text":news_p,
                "feature_img_url":featured_image_url,
                "html_table":html_table
    }
    


    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data

