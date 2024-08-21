from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime
import os
import sys
print("VERSION 2")
application_path = os.path.dirname(sys.executable)

now = datetime.now()
month_day_year = now.strftime("%m%d%Y")



website = "https://www.dailywire.com/"
path = "/usr/local/bin/chromedriver"

options = Options()
options.add_argument("--headless")

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options = options)
driver.get(website)
containers = driver.find_elements(by="xpath", value="//div[@class='Homepage_topStoriesContainer__8P1vU']//div/div")

titles = []
authors = []
links = []

for container in containers:
    try:
        title = container.find_element(by="xpath", value="./h3").text
        author = container.find_element(by="xpath", value="./p").text
        titles.append(title)
        authors.append(author)
    except:
        # Handle cases where <h3> might not be found
        print("")

my_df = pd.DataFrame({"Title": titles, "Author": authors})
file_name = f'headline--{month_day_year}.csv'
final_path = os.path.join(application_path, file_name)


my_df.to_csv(final_path, index=False)
driver.quit()