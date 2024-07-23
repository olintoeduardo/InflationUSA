from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import pandas as pd

# #initializing driver
# chromedriver_path = '/path/to/chromedriver'
# driver = webdriver.Chrome()

# try:
#     # open the page
#     driver.get("https://data.bls.gov/dataViewer/view/timeseries/CUSR0000SA0")

#     # wait for it load
#     wait = WebDriverWait(driver, 10)
#     start_year_dropdown = wait.until(EC.presence_of_element_located((By.ID, 'dv-start-year')))

#     # select 1947 for start year 
#     select = Select(start_year_dropdown)
#     select.select_by_value('1947')

#     # click the update button
#     update_button = driver.find_element(By.ID, 'dv-submit')
#     update_button.click()

#     # wait until the .CSV download button is present
#     csv_button = wait.until(EC.element_to_be_clickable((By.ID, 'csvclickCU')))

#     # click the .CSV download button
#     csv_button.click()

#     # Wait for the download to complete
#     time.sleep(5)  # Adjust the sleep time if necessary

# finally:
#     # Close the WebDriver
#     driver.quit()

download_directory = '/Users/eduardoolinto/Downloads'


files = os.listdir(download_directory)
csv_files = [f for f in files if f.endswith('.csv')]


if csv_files:
    latest_file = max(csv_files, key=lambda f: os.path.getctime(os.path.join(download_directory, f)))
    csv_file_path = os.path.join(download_directory, latest_file)

    print(f"Latest downloaded file: {latest_file}")
    df = pd.read_csv(csv_file_path,date_format=["Label"])
    print(df)

else:
    print("No CSV files found in the download directory.")