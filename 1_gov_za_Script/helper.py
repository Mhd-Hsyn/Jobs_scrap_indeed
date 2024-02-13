from bs4 import BeautifulSoup
import pandas as pd 
import os


html = """

<div class="node-content">
    
            <div class="field field--name-body field--type-text-with-summary field--label-hidden field__item"><p>The Public Service Vacancy Circular&nbsp;is published on a weekly basis (except for December) and contains the advertisements of vacant posts and jobs in Public Service departments.</p>
<p>The following jobs are advertised this week (1 December 2023):</p>
<h5 style="background-color: #004B99; line-height: 30px; color: rgb(255, 255, 255);"><strong>&nbsp;<a href="#national" style="color:#ffffff;">National</a> &nbsp;&nbsp;&nbsp;<a href="#ecape" style="color: #FFFFFF">Eastern Cape</a> &nbsp;&nbsp;&nbsp;<a href="#fs" style="color: #FFFFFF">Free State</a> &nbsp;&nbsp;&nbsp;<a href="#gau" style="color: #FFFFFF">Gauteng</a> &nbsp;&nbsp;&nbsp;<a href="#kzn" style="color:#ffffff;">KwaZulu-Natal</a>&nbsp; &nbsp; &nbsp;<a href="#lim" style="color:#ffffff;">Limpopo</a>&nbsp; &nbsp;&nbsp;<a href="#mpu" style="color:#ffffff;">Mpumalanga</a>&nbsp; &nbsp;&nbsp;<a href="#nwest" style="color:#ffffff;">North West</a>&nbsp; &nbsp;&nbsp;<a href="#ncape" style="color:#ffffff;">Northern Cape</a>&nbsp;&nbsp; &nbsp;<a href="#wcape" style="color:#ffffff;">Western Cape</a></strong></h5>
<div style="background-color:#eeeff8">
<h4><strong><a id="national" name="national"></a>National Government jobs</strong></h4>
<p><a href="/sites/default/files/Defence.pdf">Download PDF of National Government jobs</a></p>
<ul><li>Defence</li>
</ul></div>
<div style="background-color:#f5f5f5">
<h4><strong><strong><a id="ecape" name="ecape"></a>Eastern Cape Government jobs</strong></strong></h4>
<p>No advertised jobs</p>
</div>
<div style="background-color:#eeeff8">
<h4><strong><strong><a id="fs" name="fs"></a>Free State Government jobs</strong></strong></h4>
<p>No advertised jobs</p>
</div>
<div style="background-color:#f5f5f5">
<h4><strong><strong><a id="gau" name="gau"></a>Gauteng Government jobs</strong></strong></h4>
<p><a href="/sites/default/files/Gauteng_2.pdf">Download PDF of Gauteng Government jobs</a></p>
<ul><li>Gauteng Health</li>
</ul></div>
<div style="background-color:#eeeff8">
<h4><strong><strong><a id="kzn" name="kzn"></a>KwaZulu-Natal&nbsp;Government jobs</strong></strong></h4>
<p><a href="/sites/default/files/KwaZulu-Natal_0.pdf">Download PDF of KwaZulu-Natal Government jobs</a></p>
<ul><li>KwaZulu-Natal<strong>&nbsp;</strong>Health</li>
</ul></div>
<div style="background-color:#f5f5f5">
<h4><strong><strong><a id="lim" name="lim"></a>Limpopo Government jobs</strong></strong></h4>
<p><a href="/sites/default/files/Limpopo_0.pdf">Download PDF of Limpopo Government jobs</a></p>
<ul><li>Limpopo Economic Development, Environment and Tourism</li>
<li>Limpopo Social Development</li>
</ul></div>
<div style="background-color:#eeeff8">
<h4><strong><strong><a id="mpu" name="mpu"></a>Mpumalanga Government jobs</strong></strong></h4>
<p>No advertised jobs</p>
</div>
<div style="background-color:#f5f5f5">
<h4><strong><strong><a id="nwest" name="nwest"></a>North West Government jobs</strong></strong></h4>
<p>No advertised jobs</p></div>
<div style="background-color:#eeeff8">
<h4><strong><strong><a id="ncape" name="ncape"></a>Northern Cape Government jobs</strong></strong></h4>
<p><a href="/sites/default/files/Northern%20Cape.pdf">Download PDF of Northern Cape Government jobs</a></p>
<ul><li>Northern Cape Health</li>
</ul></div>
<div style="background-color:#f5f5f5">
<h4><strong><strong><a id="wcape" name="wcape"></a>Western Cape Government jobs</strong></strong></h4>
<p>No advertised jobs<br>
&nbsp;</p>
<p>Download the complete circular:&nbsp;<a href="/sites/default/files/PUBLIC%20SERVICE%20VACANCY%20CIRCULAR%2044%20OF%202023.pdf">Public Service Vacancy Circular No 44 of 1 December 2023</a> [PDF]</p>
</div>
</div>
      
  <div class="field field--name-field-related-links field--type-link field--label-above">
    <div class="field__label">Related information</div>
          <div class="field__items">
              <div class="field__item"><a href="https://www.gov.za/about-government/government-jobs">More government jobs links and information</a></div>
              </div>
      </div>

    <div class="h-px bg-gov-sharegray mt-10 "></div>
    <div class="grid grid-cols-1 md:grid-cols-2 mt-4">
      <div>
        <h3 class="mb-2 text-gov-sharegray">Share this page</h3>  
          <div class="share-icons inline-flex items-center">
            <a class="social-link facebook text-gov-sharegray" href="https://www.facebook.com/sharer.php?u=https://www.gov.za//government-jobs-week" id="fb-share" rel="nofollow noreferrer" target="_blank" title="Share on Facebook"><img alt="SAnews Facebook" class="social-link" src="/themes/custom/tailwindcss/images/fb-share-icon.svg" style="width:30px; height=30px;"><div class="inline ml-2 mr-5 text-gov-sharegray">Facebook</div></a>
            <a class="social-link twitter" href="https://twitter.com/share?url=https://www.gov.za//government-jobs-week" id="fb-share" rel="nofollow noreferrer" target="_blank" title="Share on Twitter"><img alt="SAnews Twitter" class="social-link" src="/themes/custom/tailwindcss/images/twitter-share-icon.svg" style="width:30px; height=30px;"><div class="inline ml-2 mr-5 text-gov-sharegray">Twitter</div></a>
            <a class="social-link whatsapp" href="https://api.whatsapp.com:/send?text=https://www.gov.za//government-jobs-week" data-action="share/whatsapp/share" target="_blank" title="Share on WhatsApp" rel="noreferrer"> <img alt="SAnews WhatsApp" class="social-link" src="/themes/custom/tailwindcss/images/whatsapp-share-icon.svg" style="width:30px; height=30px;"><div class="inline ml-2 mr-5 text-gov-sharegray">WhatsApp</div></a>
                      </div>
      </div>
      
      
      <div>
            </div>
      
      

    </div>
  </div>
"""


def scrap_govtjob(html):
    soup = BeautifulSoup(html, 'html.parser')
    main_div = soup.find('div', class_='field__item')
    if main_div:
        all_job_divs = main_div.find_all('div')
        data_list = []
        for job_div in all_job_divs:
            job_title_ele = job_div.find('h4')
            job_title = job_title_ele.text.strip() if job_title_ele else ''
            print(job_title)

            job_adver_ele = job_div.find('p')
            job_adver = job_adver_ele.text.strip() if job_adver_ele else ''
            print(job_adver)


            job_pdf_ele = job_div.find('a', href=True)
            job_pdf_link = f"https://www.gov.za/{job_pdf_ele['href']}" if job_pdf_ele else ''
            print(job_pdf_link)

            job_ul_ele = job_div.find('ul')
            # print(job_ul_ele)
            job_li_list = job_ul_ele.find_all('li') if job_ul_ele else ''
            advertise_list = [job_li.text.strip() for job_li in job_li_list if job_li_list ]
            print(advertise_list)

            print("\n\n\n")

            headers = ['title', 'adver', 'pdf_link', 'list']

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
            # If the CSV file doesn't exist, create a new DataFrame and save it to the CSV file
            df = pd.DataFrame(data_list, columns=['title', 'adver', 'pdf_link', 'list'])
            df.to_csv(file_path, index=False)





scrap_govtjob(html)

