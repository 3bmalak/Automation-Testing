from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as ChromeOptions

import time

URL = 'https://eg.indeed.com/?r=us'
chrome_options = ChromeOptions()
# chrome_options.add_argument("--headless")  # Uncomment this line to run in headless mode

# Make sure to provide the correct path to chromedriver if it's not in PATH
driver = webdriver.Edge( options=chrome_options)
driver.get(URL)

try:
    ccc = driver.find_element(By.XPATH, '//*[@id="mosaic-desktopserpjapopup"]/div[1]/button')
    ccc.click()
    print("Closed!")
except:
    print("Mfesh")


what = input("what : ")
whattff = driver.find_element(By.XPATH, '//*[@id="text-input-what"]')


whattff.send_keys(what)


where = input("where : ")
wheretff = driver.find_element(By.XPATH, '//*[@id="text-input-where"]')
wheretff.send_keys(where)


find_job_button = driver.find_element(By.XPATH, '//*[@id="jobsearch"]/button')
find_job_button.click()


# time.sleep(3)


ul_element = driver.find_element(By.XPATH, '//*[@id="mosaic-provider-jobcards"]/ul')

# Find all the li elements under the ul

li_elements = ul_element.find_elements(By.XPATH, './li')
print(len(li_elements))
x=0
# Print xpaths of all li elements
while x==0:

    try:
        ccc = driver.find_element(By.XPATH, '//*[@id="mosaic-desktopserpjapopup"]/div[1]/button')
        ccc.click()
        print("Closed!")
    except:
        print("Mfesh")

    for index, li in enumerate(li_elements, 1):
        # Construct the xpath for each li by using its relative position in the ul
        if index%6!=0:
            try:
                block_of_list = driver.find_element(By.XPATH, f'//*[@id="mosaic-provider-jobcards"]/ul/li[{index}]')
                block_of_list.click()
                print("------------------------------------------------")
                print("")
                print(f'//*[@id="mosaic-provider-jobcards"]/ul/li[{index}]')
                time.sleep(5)
                # // *[ @ id = "job_2f5de47969129f2e"]  //*[@id="jobsearch-ViewjobPaneWrapper"]/div/div/div/div[1]/div/div/div[2]/div[1]
                element = driver.find_element(By.XPATH,'//*[@id="jobsearch-ViewjobPaneWrapper"]/div/div/div/div[1]/div/div/div[1]')
                if element.text!="":
                    print("Job title : " , element.text.split("\n")[0])
                    print("Company Name:", element.text.split("\n")[2])
                    print("City:", element.text.split("\n")[3])
                else:
                    Job_Title = driver.find_element(By.XPATH,'//*[@id="jobsearch-ViewjobPaneWrapper"]/div/div/div/div[1]/div/div/div[2]/div[1]/h2/span')
                    Company_Name = driver.find_element(By.XPATH,'//*[@id="jobsearch-ViewjobPaneWrapper"]/div/div/div/div[1]/div/div/div[2]/div[2]/div/div/div/div[1]/div[1]/a')
                    City = driver.find_element(By.XPATH,'//*[@id="jobsearch-ViewjobPaneWrapper"]/div/div/div/div[1]/div/div/div[2]/div[2]/div/div/div/div[2]/div')
                    print("Job title : " , Job_Title.text.split("\n")[0])
                    print("Company Name:", Company_Name.text)
                    print("City:", City.text)
                Job_Description = driver.find_element(By.XPATH,'//*[@id="jobDescriptionText"]')
                print("Job title : ", Job_Description.text)
                print("")
                print("------------------------------------------------")
                print("")
            except:
                break
    try:
        next_page_button = driver.find_element(By.XPATH, '//*[@id="jobsearch-JapanPage"]/div/div/div[5]/div[1]/nav/div[6]/a')
        next_page_button.click()
        time.sleep(4)
        print("Element found!")
    except:
        x=5
        print("Element not found.")






