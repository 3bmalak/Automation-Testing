from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as ChromeOptions
import time
from selenium.webdriver.support.ui import Select


URL = 'https://www.rentometer.com/'
chrome_options = ChromeOptions()
# chrome_options.add_argument("--headless")  # Uncomment this line to run in headless mode

# Make sure to provide the correct path to chromedriver if it's not in PATH
driver = webdriver.Edge( options=chrome_options)
driver.get(URL)


try:
    SignIn = driver.find_element(By.XPATH, '//*[@id="navbar-collapse"]/ul[1]/li[2]')
    SignIn.click()
    time.sleep(3)

    email = driver.find_element(By.XPATH, '//*[@id="user_email"]')
    email.send_keys("Ahmed.Ahmed115@outlook.com")
    password = driver.find_element(By.XPATH, '//*[@id="user_password"]')
    password.send_keys("Temp159357!!")

    signInButton = driver.find_element(By.XPATH, '//*[@id="new_user"]/input[3]')
    signInButton.click()
    time.sleep(6)

except:
    print("Already logged in")


Address = input("Enter an address : ")
Addresstff = driver.find_element(By.XPATH, '//*[@id="address_unified_search_address"]')
Addresstff.send_keys(Address)

dropdown_element =  driver.find_element(By.XPATH, '//*[@id="address_unified_search_bed_style"]')
dropdown = Select(dropdown_element)
Beds = input("Enter number of beds : ")
beds=Beds+" "+"Bed"
dropdown.select_by_visible_text(beds)

try:
    analyzeButton =  driver.find_element(By.XPATH, '//*[@id="address_search_submit"]')
    analyzeButton.click()

    time.sleep(3)

    AVERAGE = driver.find_element(By.XPATH, '//*[@id="active-results-container"]/div[1]/div[1]/div[3]/div[2]/div/div/div/div/div[1]/p/abbr')
    MEDIAN = driver.find_element(By.XPATH, '//*[@id="active-results-container"]/div[1]/div[1]/div[3]/div[2]/div/div/div/div/div[2]/p/abbr')

    def extract_value(dollar_string):
        return int(dollar_string.replace("$", "").replace(",", ""))

    num_value1 = extract_value(AVERAGE.text)
    num_value2 = extract_value(MEDIAN.text)

    if num_value1 > num_value2:
        print(num_value1)
    else:
        print(num_value2)
except:
    print("Reach limited Analyze!!")

time.sleep(200)