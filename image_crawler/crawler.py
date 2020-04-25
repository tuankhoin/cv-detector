#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import selenium
import os
import time
import io
from PIL import Image
from selenium import webdriver
from bs4 import BeautifulSoup
import hashlib


# In[2]:


# setting directory for chromedriver
DRIVER_PATH = "./chromedriver"
wd = webdriver.Chrome(executable_path=DRIVER_PATH)


# In[3]:


wd.get('https://google.com')


# In[4]:


search_box = wd.find_element_by_css_selector('input.gLFyf')
search_box.send_keys('masks on face')


# In[5]:


wd.quit()


# In[6]:


# fetch images by scrolling through results
def fetch_image_urls(query:str, max_links_to_fetch:int, wd:webdriver, sleep_between_interactions:int=1):
    def scroll_to_end(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_between_interactions)    
    
    # build the google query
    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

    # load page
    wd.get(search_url.format(q=query))

    image_urls = set()
    image_count = 0
    results_start = 0
    while image_count < max_links_to_fetch:
        scroll_to_end(wd)

        # get all image thumbnail results
        thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
        number_results = len(thumbnail_results)
        
        print(f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}")
        
        for img in thumbnail_results[results_start:number_results]:
            # try to click every thumbnail such that we can get the real image behind it
            try:
                img.click()
                time.sleep(sleep_between_interactions)
            except Exception:
                continue

            # extract image urls    
            actual_images = wd.find_elements_by_css_selector('img.n3VNCb')
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    image_urls.add(actual_image.get_attribute('src'))

            image_count = len(image_urls)

            if len(image_urls) >= max_links_to_fetch:
                print(f"Found: {len(image_urls)} image links, done!")
                break
        else:
            print("Found:", len(image_urls), "image links, looking for more ...")
            time.sleep(30)
            return
            load_more_button = wd.find_element_by_css_selector(".mye4qd")
            if load_more_button:
                wd.execute_script("document.querySelector('.mye4qd').click();")

        # move the result startpoint further down
        results_start = len(thumbnail_results)

    return image_urls


# In[7]:


# function for downloading the image and raise errors whenever necessary 
def persist_image(folder_path:str,url:str):
    try:
        image_content = requests.get(url).content

    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}")

    try:
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        file_path = os.path.join(folder_path,hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=85)
        print(f"SUCCESS - saved {url} - as {file_path}")
    except Exception as e:
        print(f"ERROR - Could not save {url} - {e}")


# In[8]:


# combining the previous two functions 
# google search and download 

def search_and_download(search_term:str,driver_path:str,target_path:str,number_images):
    target_folder = os.path.join(target_path,'_'.join(search_term.lower().split(' ')))

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    with webdriver.Chrome(executable_path=driver_path) as wd:
        res = fetch_image_urls(search_term, number_images, wd=wd, sleep_between_interactions=0.5)
        
    for elem in res:
        persist_image(target_folder,elem)


# In[11]:


SEARCH_TERM_MASK = 'masks on face'
SEARCH_TERM_MASKOFF_1 = 'portrait'

TARGET_PATH = './images'


# In[12]:


# demo for 10 mask images
search_and_download(
    search_term = SEARCH_TERM_MASK,
    driver_path = DRIVER_PATH,
    target_path = TARGET_PATH,
    number_images = 10
)


# In[13]:


# demo for 10 images without mask
search_and_download(
    search_term = SEARCH_TERM_MASKOFF_1,
    driver_path = DRIVER_PATH,
    target_path = TARGET_PATH,
    number_images = 10
)

