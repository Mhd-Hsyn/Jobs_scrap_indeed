import re, time, json, random, requests
import pandas as pd
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
import os
from bs4 import BeautifulSoup
import pandas as pd 
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
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
# proxy = get_random_proxy()  # Use a function to get a random proxy

print(headers)


# Set Chrome options
options = Options()
# options.headless = False
options.add_argument('--enable-logging')
options.add_argument('--log-level=0')
# options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
options.add_argument(f'user-agent={headers["User-Agent"]}')
options.add_argument('--no-sandbox')
# options.add_argument(f'--proxy-server={proxy}')


def random_delay():
    time.sleep(random.uniform(1, 3))




def get_links(html):
    links = []
    soup = BeautifulSoup(html, 'html.parser')
    all_job_cards= soup.find_all('div', class_='module job-result')
    if all_job_cards:
        for jobcard in all_job_cards:
            job_title = jobcard.find('div', class_='job-result-title')
            a_tag = job_title.find('a', href=True)
            base_url = "https://www.careerjunction.co.za/"
            url = base_url+a_tag['href'] if a_tag else None
            url = url.strip().replace(" ", "%20") if url else None
            url = url.split('?')[0] if url and url.split('?') else None
            links.append(url)

    return links



def scrap_data(html):
    data = {
        'jobName': '',
        'companyName': '',
        'salary': '',
        'position': '',
        'location': '',
        'posted_on': '',
        'expires': '',
        'jobRef': ''
    }

    soup= BeautifulSoup(html, 'html.parser')
    target_div = soup.find('div', class_= 'cjun-main-profile job-details')
    if target_div:
        name_ele = target_div.find('div', class_='name-wrapper') 
        data['jobName'] = name_ele.find('h1').get_text(strip= True) if name_ele and name_ele.find('h1') else ''
        data['companyName'] = name_ele.find('h2').get_text(strip= True) if name_ele and name_ele.find('h2') else ''

        target_ul = target_div.find('ul', class_='job-overview')
        li_tags = target_ul.find_all('li') if target_ul else None
        if li_tags:
            for litag in li_tags:
                if 'salary' in litag.get('class',[]):
                    data['salary'] = litag.get_text(strip=True)
                elif 'position' in litag.get('class',[]):
                    data['position'] = litag.get_text(strip=True)
                elif 'location' in litag.get('class', []):
                    data['location'] = litag.get_text(strip=True)
                elif 'updated-time' in litag.get('class', []):
                    data['posted_on'] = litag.get_text(strip = True)
                elif 'expires' in litag.get('class', []):
                    data['expires'] = litag.get_text(strip=True)
                elif 'cjun-job-ref' in litag.get('class', []):
                    data['jobRef'] = litag.get_text(strip=True)

    return data





def sysInit(options):

    # Start virtual display
    display = Display(visible=0, size=(800, 600))
    # display.start()
    web_driver = None
    try:
        print("Starting........")
        web_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        web_driver.get("https://www.careerjunction.co.za/jobs/results?keywords=&autosuggestEndpoint=/autosuggest&location=0&category=&btnSubmit=%20&PerPage=100&SortBy=MostRecent")
        # web_driver.get("https://www.careerjunction.co.za/jobs/results?keywords=&autosuggestEndpoint=/autosuggest&location=0&category=&btnSubmit=%20")
        # time.sleep(5)
        # random_delay()

        all_links = []
        # time.sleep(2)
        html = web_driver.page_source
        links = get_links(html)
        all_links.extend(links)

        button_enabled = True
        while button_enabled:
            try:
                # Wait for the button with the text "Next" to be clickable
                next_button = WebDriverWait(web_driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//ul[@id='pagination']/li[last()]//a[text()='>']"))
                )

                # Scroll into view
                web_driver.execute_script("arguments[0].scrollIntoView(true);", next_button)

                # Click using JavaScript
                web_driver.execute_script("arguments[0].click();", next_button)

                # Wait for the button to become stale (i.e., replaced with a new one)
                WebDriverWait(web_driver, 10).until(
                    EC.staleness_of(next_button)
                )

                # Wait for the new "Next" button to be clickable
                next_button = WebDriverWait(web_driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//ul[@id='pagination']/li[last()]//a[text()='>']"))
                )

                html = web_driver.page_source
                links = get_links(html)
                all_links.extend(links) if links is not None else None
                # random_delay()

            except TimeoutException:
                # Catch TimeoutException and break the loop if the button is not found
                break
            # Check if the button is disabled
            button_enabled = 'disabled' not in next_button.get_attribute('class')

        
        all_data = []
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory, 'career_junction.csv')

        # Check if the CSV file exists
        if os.path.exists(file_path):
            existing_df = pd.read_csv(file_path)
            new_jobs_links = [link for link in all_links if link not in existing_df['link'].values]
            print("new links ______________",len(new_jobs_links))

            for index, link in enumerate(new_jobs_links):
                print("new jobs links")
                print(f"{index+1} ______ link start ______  {link} ")
                web_driver.get(link)
                html = web_driver.page_source
                data = scrap_data(html)
                data['link'] = link
                all_data.append(data)

            new_df = pd.DataFrame(all_data)
            existing_df = pd.concat([existing_df, new_df], ignore_index=True)

            # Save the updated DataFrame to the CSV file
            existing_df.to_csv(file_path, index=False)
        
        else :
            for index, link in enumerate(all_links):
                print("all")
                print(f"{index+1} ______ link start ______  {link} ")
                web_driver.get(link)
                html = web_driver.page_source
                data = scrap_data(html)
                data['link'] = link
                all_data.append(data)

                df = pd.DataFrame(all_data)
                df.to_csv(file_path, index=False)

        print(json.dumps(all_links))

      

    finally:
        print("QUIT WEB DRIVER ______________")
        # Stop virtual display regardless of success or failure
        # display.stop()

        # Quit the WebDriver
        if web_driver:
            web_driver.quit()


sysInit(options)