"""

Script me abi kaam chal raha h 
kuch issues h jo resolve krna h

"""


import re, time, json, random, requests
import pandas as pd
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
import os
from bs4 import BeautifulSoup
import pandas as pd 
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent


def get_random_headers():
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random,
        'Accept-Language': 'en-US, en;q=0.5'
    }
    return headers


headers = get_random_headers()

# Set Chrome options
options = Options()
# options.headless = False
options.add_argument('--enable-logging')
options.add_argument('--log-level=0')
# options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
options.add_argument(f'user-agent={headers["User-Agent"]}')
options.add_argument('--no-sandbox')


def random_delay():
    time.sleep(random.uniform(1, 3))



def get_links(html):
    alllinks= []
    soup = BeautifulSoup(html,'html.parser')
    all_jobs_card = soup.find_all('article', class_='res-1fyvkmx')
    if all_jobs_card:
        for jobcard in all_jobs_card:
            a_tag = jobcard.find('a', class_='res-7mx403', href=True)
            base_url = 'https://www.pnet.co.za'
            link = base_url+a_tag['href'] if a_tag and a_tag['href'] else ''
            link = link.strip().replace(" ", "%20") if link else None
            alllinks.append(link)

    return alllinks
            













def sysInit(options, city_name):

    # Start virtual display
    display = Display(visible=0, size=(800, 600))
    # display.start()
    web_driver = None
    try:
        print("Starting........")
        web_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        web_driver.get("https://www.pnet.co.za/")

        time.sleep(2)
        try:
            # Wait for the "Accept All" button to be present on the page with a timeout of 10 seconds
            accept_all_button = WebDriverWait(web_driver, 10).until(
                EC.presence_of_element_located((By.ID, 'ccmgt_explicit_accept'))
            )

            # Click on the "Accept All" button
            accept_all_button.click()

        except TimeoutException:
            print("Timed out waiting for the 'Accept All' button to be present")


        #  Input city name
        location_input = web_driver.find_element(By.ID, "stepstone-form-element-173-input")
        location_input.clear()
        location_input.send_keys(city_name)

        # Click the search button
        search_button = web_driver.find_element(By.CLASS_NAME, "sbr-1ywshya")
        search_button.click()
        random_delay()

        all_links = []
        links = get_links(web_driver.page_source)
        all_links.extend(links)

        button_enabled = True
        while button_enabled:
            try:
                # Wait for the button with the text "Next" to be clickable
                next_button = WebDriverWait(web_driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[aria-label="Next"]'))
                )

                # Scroll into view
                web_driver.execute_script("arguments[0].scrollIntoView(true);", next_button)

                # Click using JavaScript
                web_driver.execute_script("arguments[0].click();", next_button)

                html = web_driver.page_source
                links = get_links(html)
                print("LINKS ARE______________", links)
                all_links.extend(links) if links is not None else None
                random_delay()
                
                web_driver.execute_script("window.scrollBy(0, 500);")
                web_driver.execute_script("window.scrollBy(0, 2000);")
                time.sleep(3)
                
                # Wait for the button to become stale (i.e., replaced with a new one)
                WebDriverWait(web_driver, 10, ignored_exceptions=StaleElementReferenceException).until(
                    EC.staleness_of(next_button)
                )

                # Wait for the new "Next" button to be clickable
                next_button = WebDriverWait(web_driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[aria-label="Next"]'))
                )

                


            except TimeoutException:
                # Catch TimeoutException and break the loop if the button is not found
                break
            # Check if the button is disabled
            button_enabled = 'disabled' not in next_button.get_attribute('class')

        print(json.dumps(links))



    finally:
        print("QUIT WEB DRIVER ______________")
        # Stop virtual display regardless of success or failure
        # display.stop()

        # Quit the WebDriver
        if web_driver:
            web_driver.quit()



city_name = "Cape Town"
sysInit(options, city_name)
