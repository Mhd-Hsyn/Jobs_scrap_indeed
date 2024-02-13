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




def make_new_folder(new_folder_path, folder_name):
    """Create the folder"""
    try:
        os.makedirs(new_folder_path)
        print(f"Folder '{folder_name}' created in the current directory.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists in the current directory.")


def scrap_speeches(html):
    all_data = []

    soup = BeautifulSoup(html, 'html.parser')
    target_ul = soup.find('ul', class_='uk-list')
    if target_ul:
        all_li = target_ul.find_all('li')
        for li_tag in all_li:
            links_dict = {}
            data ={
                "link": "",
                "date": "",
                "text": "",
                "also_available_in": []
            }
            link_tag = li_tag.find('a',class_ ='uk-panel', href = True)
            link = link_tag['href'] if link_tag else ''
            link = link.strip().replace(" ", "%20")
            data['link'] = link if link else ""

            target_divs = li_tag.find_all('div', class_='uk-grid-small')
            if target_divs:
                for index, target_div in enumerate(target_divs):
                    if index == 0:
                        date_div = target_div.find('div', class_='uk-first-column')
                        date = date_div.get_text(strip= True) if date_div else None
                        data['date']= date if date else ""

                        text_div = target_div.find('div', class_='uk-width-4-5')
                        text = text_div.get_text(strip =True) if text_div else None
                        data['text'] = text if text else ""

                    if index == 1:
                        all_p_tags = target_div.find('p')
                        all_a_tags = all_p_tags.find_all('a', href=True) if all_p_tags else None
                        
                        if all_a_tags:
                            for a_tag in all_a_tags:
                                # Assuming language names are within the <a> tag text
                                language_name = a_tag.text.strip()
                                pdf_link = a_tag['href']
                                links_dict[language_name] = pdf_link

                            data['also_available_in'] = [links_dict]

            all_data.append(data)
    return all_data





def updating_csvs(all_data, name):

    current_dir= os.getcwd()
    new_dir = os.path.join(current_dir, "2_dpsa_govt")
    make_new_folder(new_dir, "2_dpsa_govt")

    file_path = os.path.join(new_dir, f"{name}.csv")
    if os.path.exists(file_path):
        existing_df = pd.read_csv(file_path)
        # Check if each job title already exists in the CSV file
        new_data = [data for data in all_data if data['link'] not in existing_df['link'].values]
        # If there are new jobs, append them to the existing DataFrame
        if new_data:
            new_df = pd.DataFrame(new_data)
            existing_df = pd.concat([existing_df, new_df], ignore_index=True)
            # Save the updated DataFrame to the CSV file
            existing_df.to_csv(file_path, index=False)
        else:
            print("No new jobs")
    else:
        # If the CSV file doesn't exist, create a new DataFrame and save it to the CSV file
        df = pd.DataFrame(all_data, columns=['date', 'link', 'text', 'also_available_in'])
        df.to_csv(file_path, index=False)





def sysInit(options):

    # Start virtual display
    display = Display(visible=0, size=(800, 600))
    # display.start()
    web_driver = None
    try:
        print("Starting........")
        web_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        web_driver.get("https://www.dpsa.gov.za/newsroom/speeches/")
        html =web_driver.page_source
        all_data = scrap_speeches(html)
        updating_csvs(all_data= all_data, name="speeches")

        web_driver.get("https://www.dpsa.gov.za/newsroom/media_statements/")
        html = web_driver.page_source
        all_data = scrap_speeches(html)
        updating_csvs(all_data, "media_statements")




    finally:
        print("QUIT WEB DRIVER ______________")
        # Stop virtual display regardless of success or failure
        # display.stop()

        # Quit the WebDriver
        if web_driver:
            web_driver.quit()


sysInit(options)