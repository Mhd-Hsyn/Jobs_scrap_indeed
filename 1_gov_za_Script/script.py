import re, time, json
import pandas as pd
from selenium import webdriver
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


# Set Chrome options
options = Options()
# options.headless = False
options.add_argument('--enable-logging')
options.add_argument('--log-level=0')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
options.add_argument('--no-sandbox')

url = "https://www.gov.za/government-jobs-week"




def scrap_govtjob(html):
    soup = BeautifulSoup(html, 'html.parser')
    main_div = soup.find('div', class_='field__item')
    if main_div:
        all_job_divs = main_div.find_all('div')
        data_list = []
        for job_div in all_job_divs:
            job_title_ele = job_div.find('h4')
            job_title = job_title_ele.text.strip() if job_title_ele else ''

            job_adver_ele = job_div.find('p')
            job_adver = job_adver_ele.text.strip() if job_adver_ele else ''


            job_pdf_ele = job_div.find('a', href=True)
            job_pdf_link = f"https://www.gov.za/{job_pdf_ele['href']}" if job_pdf_ele else ''

            job_ul_ele = job_div.find('ul')
            job_li_list = job_ul_ele.find_all('li') if job_ul_ele else ''
            advertise_list = [job_li.text.strip() for job_li in job_li_list if job_li_list ]

            data_list.append({
                'title': job_title,
                'adver': job_adver,
                'pdf_link': job_pdf_link,
                'list': advertise_list
            })

        # Get the current working directory
        current_directory = os.getcwd()

        # Create the file path for the CSV file in the current directory
        file_path = os.path.join(current_directory, 'govt_jobs_data.csv')

        # Check if the CSV file exists
        if os.path.exists(file_path):
            # Read the existing data from the CSV file
            existing_df = pd.read_csv(file_path)

            # Check if each job title already exists in the CSV file
            new_jobs = [job for job in data_list if job['title'] not in existing_df['title'].values]

            # If there are new jobs, append them to the existing DataFrame
            if new_jobs:
                new_df = pd.DataFrame(new_jobs)
                existing_df = pd.concat([existing_df, new_df], ignore_index=True)

                # Save the updated DataFrame to the CSV file
                existing_df.to_csv(file_path, index=False)
            else:
                print("No new jobs")
        else:
            # If the CSV file doesn't exist, create a new DataFrame and save it to the CSV file
            df = pd.DataFrame(data_list, columns=['title', 'adver', 'pdf_link', 'list'])
            df.to_csv(file_path, index=False)






def sysInit(options, url):
    # Start virtual display
    display = Display(visible=0, size=(800, 600))
    # display.start()
    web_driver = None
    try:
        print("Starting........")
        web_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

        web_driver.get(url)
        html = web_driver.page_source
        scrap_govtjob(html)
        
    finally:
        print("QUIT WEB DRIVER ______________")
        # Stop virtual display regardless of success or failure
        # display.stop()

        # Quit the WebDriver
        if web_driver:
            web_driver.quit()


sysInit(options, url)