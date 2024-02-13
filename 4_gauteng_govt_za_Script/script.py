import re, time, json
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
import os
from bs4 import BeautifulSoup
import pandas as pd 
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
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

url = "https://jobs.gauteng.gov.za/Public/Jobs.aspx"



def getlinks(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', id = "tblJobs")
    links = []
    if table:
        rows = table.find_all('tr', class_= ['even', 'odd'])
        all_td = [row.find('td', string='View') for row in rows]
        base_url = "https://jobs.gauteng.gov.za/Public/"
        links = [ base_url+td.find('a')['href'] for td in all_td  if td.find('a')['href'] ]
    
    return links


def scrap_data(html):
    data = {
        'link': '',
        'reference_no' : '',
        'directorate' : '',
        'no_of_posts' : '',
        'package': '',
        'enquiries': '',
        'requirements': '',
        'duties': '',
        'notes': '',
        'employer': '',
        'location':'',
        'closing_date':'',
        'criteria_question': [],
        'please_note': ''
    }

    soup = BeautifulSoup(html, 'html.parser')

    main_div = soup.find('div', class_='contentbody')
    if main_div:
        ref_ele = main_div.find('span', id= 'body_lblRefNo')
        data['reference_no'] = ref_ele.text.strip() if ref_ele else ''

        direc_ele = main_div.find('span', id= 'body_lblDirectorate')
        data['directorate'] = direc_ele.text.strip() if direc_ele else ''

        no_of_posts_ele = main_div.find('span', id='body_lblNumPosts')
        data['no_of_posts'] = no_of_posts_ele.text.strip() if no_of_posts_ele else ''

        package_ele = main_div.find('span', id='body_lblPackage')
        data['package'] = package_ele.text.strip() if package_ele else ''

        enquiries_ele = main_div.find('span', id ='body_lblEnquiries')
        data['enquiries'] = enquiries_ele.text.strip() if enquiries_ele else ''

        requirement_ele = main_div.find('span', id='body_lblRequirements')
        data['requirements'] = requirement_ele.text.strip() if requirement_ele else ''

        duties_ele = main_div.find('span', id='body_lblDuties')
        data['duties'] = duties_ele.text.strip() if duties_ele else ''

        notes_ele = main_div.find('span', id ='body_lblNotes')
        data['notes'] = notes_ele.text.strip() if notes_ele else ''

        employer_ele = main_div.find('span', id='body_lblDept')
        data['employer'] = employer_ele.text.strip() if employer_ele else ''

        location_ele = main_div.find('span', id='body_lblCentre')
        data['location'] = location_ele.text.strip() if location_ele else ''

        closing_ele = main_div.find('span', id ='body_lblClosingDate')
        data['closing_date'] = closing_ele.text.strip() if closing_ele else ''

        question_ele = main_div.find('table', id ='body_GridCriteria')
        rows = question_ele.find_all('tr') if question_ele else ''
        data['criteria_question'] = [row.find('td').text.strip() for row in rows if rows and row.find('td')]

        # Find the div containing the p tag with the specified text
        target_div = soup.find('p', string='Please Notes : ')
        ultag = target_div.find_next_sibling('ul') if target_div else None
        litag = ultag.find('li') if ultag else None
        data['please_note'] = litag.get_text(strip=True) if litag else ''

    return data








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
        all_links = []
        all_links.extend(getlinks(html))
        button_enabled = True
        while button_enabled:
            try:
                # Wait for the button with the text "Next" to be clickable
                next_button = WebDriverWait(web_driver, 20).until(
                    EC.element_to_be_clickable((By.ID, 'tblJobs_next'))
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
                    EC.element_to_be_clickable((By.ID, 'tblJobs_next'))
                )

                html = web_driver.page_source
                links = getlinks(html)
                all_links.extend(links) if links is not None else None

            except TimeoutException:
                # Catch TimeoutException and break the loop if the button is not found
                break
            # Check if the button is disabled
            button_enabled = 'disabled' not in next_button.get_attribute('class')


        
        current_directory = os.getcwd()

        # Create the file path for the CSV file in the current directory
        file_path = os.path.join(current_directory, 'gpg_prof_job.csv')

        # Check if the CSV file exists
        if os.path.exists(file_path):
            existing_df = pd.read_csv(file_path)
            new_jobs_links = [link for link in all_links if link not in existing_df['link'].values]
            print("new links ______________",len(new_jobs_links))

            all_data = []

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


sysInit(options, url)