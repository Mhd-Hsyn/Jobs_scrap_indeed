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



# def get_proxies():
#     try:
#         response = requests.get('https://www.proxy-list.download/api/v1/get?type=https')
#         if response.status_code == 200:
#             proxies = response.text.split('\r\n')
#             return proxies
#         else:
#             return None
#     except Exception as e:
#         print("Error fetching proxies:", e)
#         return None

# def get_random_proxy():
#     proxies = get_proxies()
#     print("Available Proxies:", proxies)

#     if proxies:
#         return random.choice(proxies)
#     else:
#         raise Exception("No proxies available")





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
# print(proxy)


# headers = {
#     'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47",
#     'Accept-Language': 'en-US, en;q=0.5'
# }


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
    all_job_cards= soup.find_all('div', class_='job-card')
    if all_job_cards:
        for jobcard in all_job_cards:
            a_tag = jobcard.find('a', href=True)
            base_url = "https://www.careers24.com/"
            url = base_url+a_tag['href'] if a_tag else None
            url = url.strip().replace(" ", "%20") if url else None
            url = url.split('?')[0] if url and url.split('?') else None
            links.append(url)
    
    return links



def scrap_data(html):
    data = {
        'job_title': '',
        'location': '',
        'salary': '',
        'job_type': '',
        'sectors': '',
        'reference': '',
        'benefits': '',
        'jobApply': '',
        'employer': ''
    }
    
    soup = BeautifulSoup(html, 'html.parser')

    # Job Title
    target_h1 = soup.find('h1', class_='vacancy-detail-head')
    span = target_h1.find('span') if target_h1 else None
    data['job_title'] = span.get_text(strip=True) if span else ''

    # Additional Information
    ul = soup.find('ul', class_='small-text icon-list mb-15 w-100')
    if ul:
        li_items = ul.find_all('li')
        for li in li_items:
            icon_container = li.find('span', class_='icon-container')
            if icon_container:
                icon_class = icon_container.find('i')['class'][1]  # Extract the icon class

                if 'fa-map-marker-alt' in icon_class:
                    # Location
                    location = li.find('a')
                    data['location'] = location.get_text(strip=True) if location else ''
                elif 'fa-money-bill-alt' in icon_class:
                    # Salary
                    data['salary'] = li.get_text(strip=True).replace('Salary:', '').strip()
                elif 'fa-briefcase' in icon_class:
                    # Job Type
                    data['job_type'] = li.get_text(strip=True).replace('Job Type:', '').strip()
                elif 'fa-chart-pie' in icon_class:
                    # Sectors
                    sectors = li.find_all('a')
                    data['sectors'] = [sector.get_text(strip=True) for sector in sectors]
                elif 'fa-file-alt' in icon_class:
                    # Reference
                    data['reference'] = li.get_text(strip=True).replace('Reference:', '').strip()
                elif 'fa-plus-square' in icon_class:
                    # Benefits
                    benefits = li.find('span', class_='icon-container').find_next('span')
                    data['benefits'] = [benefit.get_text(strip=True) for benefit in benefits if benefit.get_text(strip=True) != 'Benefits:' and benefit.get_text(strip=True) != '']

    
    target_div = soup.find('div', class_='smallest-text')
    data['jobApply'] = target_div.find('p').get_text(strip=True) if target_div and target_div.find('p') else ""

    target_div_employer = soup.find('div', class_='c24-vacancy-details')
    employer_p_tag = target_div_employer.find('p', class_='mb-15') if target_div_employer else None

    if employer_p_tag and 'Employer:' in employer_p_tag.get_text():
        data['employer'] = employer_p_tag.find('a').get_text(strip=True) if employer_p_tag.find('a') else ""
    else:
        data['employer'] = ""

    return data










def sysInit(options):

    # Start virtual display
    display = Display(visible=0, size=(800, 600))
    # display.start()
    web_driver = None
    try:
        print("Starting........")
        web_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        web_driver.get("https://www.careers24.com/")
        time.sleep(5)

        # # Wait for the Cloud-Flare checkbox to be present
        # try:
        #     checkbox_xpath = "//label[contains(@class, 'ctp-checkbox-label')]"
        #     checkbox = WebDriverWait(web_driver, 30).until(
        #         EC.presence_of_element_located((By.XPATH, checkbox_xpath))
        #     )

        #     # Check if the checkbox is visible and enabled before clicking
        #     if checkbox.is_displayed() and checkbox.is_enabled():
        #         # Use JavaScript to click the checkbox
        #         web_driver.execute_script("arguments[0].click();", checkbox)
        #         print("Checkbox clicked using JavaScript.")
        #     else:
        #         print("Checkbox not visible or not enabled.")
        # except TimeoutException:
        #     print("No cloudflare")

        random_delay()

        #  Input city name
        city_name = "Cape Town"
        location_input = web_driver.find_element(By.ID, "LocationInput")
        location_input.clear()
        location_input.send_keys(city_name)

        # Click the search button
        search_button = web_driver.find_element(By.ID, "btnSearch")
        search_button.click()
        random_delay()

        all_links = []
        time.sleep(2)
        html = web_driver.page_source
        links = get_links(html)
        all_links.extend(links)

        button_enabled = True
        while button_enabled:
            try:
                # Wait for the button with the text "Next" to be clickable
                next_button = WebDriverWait(web_driver, 20).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, 'page-item.next'))
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
                    EC.element_to_be_clickable((By.CLASS_NAME, 'page-item.next'))
                )

                html = web_driver.page_source
                links = get_links(html)
                all_links.extend(links) if links is not None else None
                random_delay()

            except TimeoutException:
                # Catch TimeoutException and break the loop if the button is not found
                break
            # Check if the button is disabled
            button_enabled = 'disabled' not in next_button.get_attribute('class')

        print(json.dumps(all_links))

        all_data = []

        # 1st check the links in csvs 
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory, 'careers24.csv')

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


    finally:
        print("QUIT WEB DRIVER ______________")
        # Stop virtual display regardless of success or failure
        # display.stop()

        # Quit the WebDriver
        if web_driver:
            web_driver.quit()


sysInit(options)