import os
import time
import shutil
import threading
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

chrome_driver_dir = './.Driver'
chrome_driver_path = '/Users/srikar/anaconda3/lib/python3.11/site-packages/chromedriver_binary'

# if not os.path.exists(chrome_driver_path):
#     default_chrom_driver_path = ChromeDriverManager().install()
#     os.mkdir(chrome_driver_dir)
#     shutil.move(default_chrom_driver_path, chrome_driver_path)

# service = Service(chrome_driver_path)

chrome_options = Options()
chrome_options.add_argument('user-agent=genie-user')
chrome_options.add_argument("--headless")

def get_page_content(url):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    page_content = driver.page_source
    driver.quit()
    if(page_content == ''):
        time.sleep(1)
        return get_page_content(url)
    return page_content

def download_pdf(url, download_dir):
    try:
        temp_dir = './.Driver/cache/download_' + str(threading.get_ident())
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        os.makedirs(temp_dir)

        prefs = {"download.default_directory" : temp_dir}
        chrome_options.add_experimental_option('prefs', prefs)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        driver.get(url)

        while True: 
            downloaded = False
            file_name = None
            for file in os.listdir(temp_dir):
                if file.endswith('.pdf'):
                    downloaded = True
                    file_name = file
            if downloaded:
                break
            time.sleep(0.1)
        
        shutil.move(os.path.join(temp_dir, file_name), os.path.join(download_dir, file_name))
        shutil.rmtree(temp_dir)
        driver.quit()
        return True
    except Exception as e:
        print('Got exception ' + str(e) + ' while downloading from ' + url)
        return False

def bulk_download_pdfs(arg_list):
    url_list = []
    download_dir_list = []
    for url, download_dir in arg_list:
        url_list.append(url)
        download_dir_list.append(download_dir)
    
    with ThreadPoolExecutor() as executor:
        results = list(tqdm(executor.map(download_pdf, url_list, download_dir_list), total=len(arg_list)))
    