"""
za indeed test for deploy
"""

import time
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set Chrome options
options = Options()
# options.headless = True
options.add_argument('--enable-logging')
options.add_argument('--log-level=0')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
options.add_argument('--no-sandbox')
options.add_argument('--disable-http2')  # Disable HTTP/2


def sysInit():
    display = Display(visible=0, size=(800, 600))
    display.start()
    try:
        # Initialize the Chrome WebDriver
        web_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        # Navigate to the target URL
        web_driver.get("https://za.indeed.com/")
        time.sleep(2)

        html = web_driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        home_ele = soup.find('a', id="FindJobs")
        home = home_ele.text.strip() if home_ele else ''

        company_ele = soup.find('a', id="CompanyReviews")
        company_review = company_ele.text.strip() if company_ele else ''

        findSal_ele = soup.find('a', id="FindSalaries")
        find_sal = findSal_ele.text.strip() if findSal_ele else ''

        if home and company_review and find_sal:
            print("\n\n ********** CONGRATS WEBSITE IS OPEN ********* \n")
            print(f"BUTTON 1  IS_____________ {home}\n\n")
            print(f"BUTTON 2  IS_____________ {company_review}\n\n")
            print(f"BUTTON 3  IS_____________ {find_sal}\n\n")

        else:
            print("\n\n________ problem in fetching the title _______\n\n")
            print(html)
            print("\n\n\n_______ problem in fetching the title _______\n\n")


        time.sleep(2)

    finally:
        print("QUIT WEB DRIVER ______________")
        display.stop()
        if web_driver:
            web_driver.quit()

sysInit()
            
            