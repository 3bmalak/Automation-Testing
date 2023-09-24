from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as ChromeOptions

import time

URL = 'https://riskfactor.com/'
chrome_options = ChromeOptions()
# chrome_options.add_argument("--headless")  # Uncomment this line to run in headless mode

# Make sure to provide the correct path to chromedriver if it's not in PATH
driver = webdriver.Edge( options=chrome_options)
driver.get(URL)


ZIPCode = input("Enter ZIP Code : ")
ZIPCodetff = driver.find_element(By.XPATH, '//*[@id="searchbox"]')
ZIPCodetff.send_keys(ZIPCode)
time.sleep(3)
ZIPCodepress = driver.find_element(By.XPATH, '/html/body/div/main/div[1]/div[1]/div/div/div[2]/div/div[2]/form/div/ul/li[1]/ul')
ZIPCodepress.click()
time.sleep(5)

try:
    for i in range(2, 6):
        xpath_expression = f'//*[@id="header"]/div[2]/div/div/div/div/div[1]/div[{i}]'
        tab = driver.find_element(By.XPATH, xpath_expression)
        tabsplit = tab.text.split("\n")
        if "/10" not in tab.text:
            raise ValueError("The string contains '/10'.")


        tab.click()
        time.sleep(10)
        s=""

        if i==2:
            # time.sleep(7)
            overview=driver.find_element(By.XPATH,'/html/body/div/main/div[2]/div[2]/div[1]/div/div/div/div/div[2]/p/strong[1]/span/span')
            s=overview.text.split(" ")[0]
        if i==3:
            # time.sleep(10)
            overview=driver.find_element(By.XPATH,'//*[@id="wildfire_risk_overview"]/div/div/div/div[1]/div[2]/p/strong/span/span')
            s=overview.text.split(" ")[0]

        if i==4:
            overview=driver.find_element(By.XPATH,'//*[@id="wind_risk_overview"]/div/div/div/div[2]/p/strong/span/span/span')
            s=overview.text.split(" ")[0]

        if i==5:
            overview=driver.find_element(By.XPATH,'//*[@id="heat_risk_overview"]/div/div/div[1]/div[2]/div/article/div/div/p/strong/span/span')
            s=overview.text.split(" ")[0]
        print(tabsplit[0] +' : '+ tabsplit[1]+" "+ s)

except:
    for i in range(1, 5):
        xpath_expression = f'//*[@id="header"]/div[2]/div/div/div/div/div[1]/div[{i}]'
        tab = driver.find_element(By.XPATH, xpath_expression)
        tabsplit=tab.text.splitlines()
        tab.click()

        time.sleep(10)
        s=""

        if i==1:
            # time.sleep(7)
            overview=driver.find_element(By.XPATH,'//*[@id="flood_risk_overview"]/div/div/div[3]/div[2]/div[2]/div/div/div/span/strong/b')
            s=overview.text.split(" ")[0]
        if i==2:
            # time.sleep(10)
            overview=driver.find_element(By.XPATH,'//*[@id="wildfire_risk_overview"]/div/div/div[3]/div[2]/div[2]/div/div/div/span/strong/b')
            s=overview.text.split(" ")[0]

        if i==3:
            overview=driver.find_element(By.XPATH,'//*[@id="wind_risk_overview"]/div/div/div/div[2]/article/div/div/p/strong[1]/span/span/span')
            s=overview.text.split(" ")[0]

        if i==4:
            overview=driver.find_element(By.XPATH,'//*[@id="heat_risk_overview"]/div/div/div[1]/div[2]/article/div/div/p[1]/strong[2]')
            s=overview.text.split(" ")[0]
        print(tabsplit[0] +' : '+  s)


    # print("fffffffffffff")
