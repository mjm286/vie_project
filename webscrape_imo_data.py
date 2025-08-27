"""
function to webscrape and collect data about vessel based on her imo.
"""

from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

import numpy as np
import requests
import pandas as pd
import json
import ast


def scrape_data(imo_tag):
    print(imo_tag)
    data = {
        "imo":imo_tag,
        "name":np.nan,
        "ship_type": np.nan,
        "build_year": np.nan,
        "gross_tonnage": np.nan,
        "DWT": np.nan
    }
    try:
        firefox_driver = r'C:\Users\matth\OneDrive\Documents\vie_project\geckodriver.exe'
        firefox_service = Service(firefox_driver) 
        firefox_options = Options()
        firefox_options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

        url = "" # insert certain website to scrape DWT

        driver = webdriver.Firefox(service=firefox_service, options=firefox_options)
        driver.get(url)
        time.sleep(2)
        search_imo_input = driver.find_element(By.ID, "advsearch-name")
        time.sleep(1)
        search_imo_input.clear()
        time.sleep(1)
        search_imo_input.send_keys(imo_tag)
        time.sleep(1)
        search_imo_input.send_keys(Keys.ENTER)
        time.sleep(4)
        tanker_name = driver.find_element(By.CLASS_NAME, "slna")
        data["name"] = tanker_name.text
        time.sleep(2)
        tanker_type = driver.find_element(By.CLASS_NAME, "slty")
        data["ship_type"] = tanker_type.text
        time.sleep(2)
        data["build_year"] = driver.find_element(By.XPATH,"//table[@class='results']/tbody/tr/td[2]").text
        time.sleep(2)
        data["gross_tonnage"] = driver.find_element(By.XPATH,"//table[@class='results']/tbody/tr/td[3]").text
        time.sleep(2)
        data["DWT"] = driver.find_element(By.XPATH,"//table[@class='results']/tbody/tr/td[4]").text
        time.sleep(4)
        print(f"{data}")
        driver.quit()
        return data
    
    except Exception as e:
        print(f"{e}")
        driver.quit()
        return data
