
import re, time, json, random, requests
import pandas as pd
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
import os
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urlparse, parse_qs
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
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

    soup = BeautifulSoup(html, 'html.parser')
    target_ul = soup.find('ul', class_='css-zu9cdh eu4oa1w0')
    all_li_tags = target_ul.find_all('li', class_='css-5lfssm eu4oa1w0') if target_ul else ''
    base_url = 'https://za.indeed.com'
    linklist = [base_url + litag.find('a', href=True)['href'] for litag in all_li_tags if litag.find('a', href=True)]

    return linklist
        


def scrap_data(html):
    data = {
        "job_title": "",
        "company_name": "",
        "company_location": "",
        "salary": "",
        "job_type": "",
        "job_description_html": ""
    }

    soup = BeautifulSoup(html, 'html.parser')
    target_h1 = soup.find('h1', {"data-testid":"jobsearch-JobInfoHeader-title"})
    data['job_title'] = target_h1.getText(strip=True) if target_h1 else ""
    print("\n\nJob Title is : _____  ", data['job_title'])

    target_div = soup.find('div', {"data-testid":"inlineHeader-companyName"})
    data['company_name'] = target_div.get_text(strip= True) if target_div else ""
    print("Company Name: ______ ", data['company_name'])

    location_div = soup.find('div', {"data-testid":"inlineHeader-companyLocation"})
    data['company_location'] = location_div.find('div').get_text(strip=True) if location_div and location_div.find('div') else ""
    print("Company Location: ______ ", data['company_location'])

    salary_jobtype_ele = soup.find('div', id="salaryInfoAndJobType")
    salary_ele = salary_jobtype_ele.find('span', class_="css-19j1a75") or salary_jobtype_ele.find('span', class_="css-2iqe2o") if salary_jobtype_ele else None
    data['salary'] = salary_ele.get_text(strip= True) if salary_ele else ""
    print("\n\n",salary_jobtype_ele)
    print("\n\n",salary_ele, "\n\n")

    jobtype_ele = salary_jobtype_ele.find('span', class_= "css-k5flys") if salary_jobtype_ele else None
    data['job_type'] = jobtype_ele.get_text(strip=True) if jobtype_ele else ""

    print("JobType: ______ ", data['job_type'])
    print("Salary: ______ ", data['salary'])

    job_desript_ele = soup.find('div', {'id':"jobDescriptionText"})
    data['job_description_html'] = str(job_desript_ele)

    return data



def sysInit(options, city_name):

    # Start virtual display
    display = Display(visible=0, size=(800, 600))
    # display.start()
    web_driver = None
    try:
        print("Starting........")
        web_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        web_driver.get("https://za.indeed.com/")
        time.sleep(5)

        # try:
        #      # Locate the iframe
        #     iframe = web_driver.find_element(By.XPATH, "//iframe[contains(@src, 'accounts.google.com')]")

        #     # Remove the 'overflow: hidden' style from the iframe
        #     web_driver.execute_script("arguments[0].style.overflow = 'visible';", iframe)

        #     # Switch to the iframe
        #     web_driver.switch_to.frame(iframe)

        #     # Wait for the "Continue" button to be clickable
        #     continue_button = WebDriverWait(web_driver, 10).until(
        #         EC.element_to_be_clickable((By.ID, "continue"))
        #     )

        #     # Click the "Continue" button
        #     continue_button.click()
        # except TimeoutException:
        #     print("Popup did not appear within the specified time.")
        #     pass
        # except NoSuchElementException:
        #     print("Close button not found in the popup.")
        #     pass

        #  Input city name
        location_input = web_driver.find_element(By.ID, "text-input-where")
        location_input.clear()
        location_input.send_keys(city_name)

        # Click the search button
        search_button = web_driver.find_element(By.CLASS_NAME, "yosegi-InlineWhatWhere-primaryButton")
        search_button.click()
        random_delay()
        time.sleep(5)
        all_links = []
        web_driver.execute_script("window.scrollBy(0, 1000);") 
        time.sleep(2)
        web_driver.execute_script("window.scrollBy(0, 2500);") 
        time.sleep(2)
        
        links = get_links(web_driver.page_source)
        all_links.extend(links)

        count = 0
        button_enabled = True
        while button_enabled and count<10:
            try:
                # Wait for the button with the text "Next" to be clickable
                next_button = WebDriverWait(web_driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '//a[@data-testid="pagination-page-next"]'))
                )
                # Scroll into view
                web_driver.execute_script("arguments[0].scrollIntoView(true);", next_button)

                # Click using JavaScript
                web_driver.execute_script("arguments[0].click();", next_button)

                try:
                    close_button = WebDriverWait(web_driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.css-yi9ndv.e8ju0x51'))
                    )
                    # Click the close button
                    close_button.click()
                except TimeoutException:
                    pass

                # Wait for the button to become stale (i.e., replaced with a new one)
                WebDriverWait(web_driver, 10).until(
                    EC.staleness_of(next_button)
                )

                # Wait for the new "Next" button to be clickable
                next_button = WebDriverWait(web_driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//a[@data-testid="pagination-page-next"]'))
                )

                time.sleep(2)
                web_driver.execute_script("window.scrollBy(0, 1000);") 
                time.sleep(2)
                html = web_driver.page_source
                web_driver.execute_script("window.scrollBy(0, 2500);") 
                time.sleep(2)
                html = web_driver.page_source
                links = get_links(html)
                all_links.extend(links) if links is not None else None
                random_delay()
                count +=1

            except TimeoutException:
                # Catch TimeoutException and break the loop if the button is not found
                break
            # Check if the button is disabled
            button_enabled = 'disabled' not in next_button.get_attribute('class')


        # all_links = [
        #     ' https://za.indeed.com/rc/clk?jk=5d1422a7c10176f1&bb=Icbks5iFzE0UOWcJ1alnUpKMBFvdSgy1qjTm46pZZe01UB2u923SZYj2pG-gp8uaNr09L2h3VcgOi1V3gZsDT5xBbqzA5jNSM9-hezTfPrs%3D&xkcb=SoBE67M3G-nxSHynYx0MbzkdCdPP&fccid=47c8e42bc369fd2c&vjs=3',
        #     'https://za.indeed.com/viewjob?jk=05dcbcb388fe4af2&from=serp&vjs=3',
        #     'https://za.indeed.com/viewjob?jk=ee97b711c7e5b961&tk=1hjrnefgcjtsk800&from=serp&vjs=3',
        #     'https://za.indeed.com/rc/clk?jk=ee97b711c7e5b961&bb=zahgjgiVeTUS7JyrlRXUBVVwC7axFzPIhyJrZgDQTu9lHYfuZem8o_Jjldmi3OFPDzcrGcqc6iBrvpn4iZrgJq_NuGMsKMhlrWC98DTBjfE%3D&xkcb=SoAJ67M3G7m2KMR9Np0LbzkdCdPP&fccid=a8f020997cd25271&vjs=3',
        #     'https://za.indeed.com/viewjob?jk=4fff6be7bc1d6aaa&tk=1hjs0b3uakcq0800&from=serp&vjs=3',
        # ]

        print(json.dumps(all_links))
        all_data = []

        current_directory = os.getcwd()
        file_path = os.path.join(current_directory, 'za_indeed.csv')

        # Check if the CSV file exists
        if os.path.exists(file_path):
            existing_df = pd.read_csv(file_path)
            jk_values = [parse_qs(urlparse(link).query)['jk'][0] for link in all_links]
            print("\n",jk_values)
            new_jobs_links = [link for link, jk in zip(all_links, jk_values) if jk not in existing_df['link'].str.extract(r'jk=([^&]+)')[0].values]

            print("new links ______________",len(new_jobs_links))

            for index, link in enumerate(new_jobs_links):
                time.sleep(2)
                print("new jobs links")
                print(f"{index+1} ______ link start ______  {link} ")
                web_driver.get(link)
                time.sleep(3)
                html = web_driver.page_source
                web_driver.execute_script("window.scrollBy(0, 500);") 
                time.sleep(2)
                html = web_driver.page_source
                web_driver.execute_script("window.scrollBy(0, 1000);") 
                time.sleep(2)
                html = web_driver.page_source
                web_driver.execute_script("window.scrollBy(0, 1);") 
                time.sleep(2)
                
                html = web_driver.page_source
                data = scrap_data(html)
                if all(value == "" for value in data.values()):
                    # If all fields are empty, continue to the next iteration
                    print("\n\n******************************************************")
                    print("\nCheck the link I think cloud-flare is come \n", link)
                    continue
                data['link'] = link
                all_data.append(data)
                time.sleep(5)

                old_df = pd.read_csv(file_path)
                new_df = pd.DataFrame([data])
                final_df = pd.concat([old_df, new_df], ignore_index=True)

                # Save the updated DataFrame to the CSV file
                final_df.to_csv(file_path, index=False)

        
        else :
            for index, link in enumerate(all_links):
                print("all")
                print(f"{index+1} ______ link start ______  {link} ")
                time.sleep(2)
                web_driver.get(link)
                time.sleep(3)
                html = web_driver.page_source
                web_driver.execute_script("window.scrollBy(0, 500);") 
                time.sleep(2)
                html = web_driver.page_source
                web_driver.execute_script("window.scrollBy(0, 1000);") 
                time.sleep(2)
                html = web_driver.page_source
                web_driver.execute_script("window.scrollBy(0, 1);") 
                time.sleep(2)

                html = web_driver.page_source
                data = scrap_data(html)
                if all(value == "" for value in data.values()):
                    # If all fields are empty, continue to the next iteration
                    print("\n\n******************************************************")
                    print("\nCheck the link I think cloud-flare is come \n", link)
                    continue
                data['link'] = link
                all_data.append(data)
                df = pd.DataFrame(all_data)
                df.to_csv(file_path, index=False)
                time.sleep(5)



    finally:
        print("QUIT WEB DRIVER ______________")
        # Stop virtual display regardless of success or failure
        # display.stop()

        # Quit the WebDriver
        if web_driver:
            web_driver.quit()



city_name = "Cape Town"
sysInit(options, city_name)

