from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import requests
import time
#from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

edge_path = "C:\\Users\\AA\Downloads\\edgedriver_win64\\msedgedriver.exe"
service = Service(executable_path= edge_path)
wd = webdriver.Edge(service = service)
print(wd.title)
print(wd.current_url)
wd.get("https://www.thesparksfoundationsingapore.org/")
print("\nTest Cases")

# TestCase 1: Title
print("\nTestCase 1:")
if wd.title:
    print("\nSuccess! ", wd.title)
else:
    print("\nTitle Verification Failed!\n")

# TestCase 2: To find logo of the webpage
print("\nTestCase 2:")
try:
    wd.find_element(By.XPATH,'//*[@id="home"]/div/div[1]/h1/a/*')
    print('Success!\n')
    time.sleep(3)
except NoSuchElementException:
    print('logo verification failed!!\n')

# TestCase 3: Check if navbar appears
print("TestCase 3:")
try:
    wd.find_element(By.CLASS_NAME,"navbar")
    print("Success!!\n")
except NoSuchElementException:
    print("Navbar Verification Failed!\n")

# TestCase 4: Home button
print("TestCase 4:")
try:
    wd.find_element(By.PARTIAL_LINK_TEXT,"The Sparks Foundation")
    print("Success!\n")
except NoSuchElementException:
    print("Failed!\n")

# TestCase 5: About Us Page
print("TestCase 5:")
try:
    wd.find_element(By.LINK_TEXT,'About Us').click()
    time.sleep(3)
    wd.find_element(By.LINK_TEXT,'Corporate Partners').click()
    time.sleep(3)
    print('Success!\n')
except NoSuchElementException:
    print("Page visit Failed! Does not exist.\n")
    time.sleep(3)

# TestCase 6: Policy page
print('TestCase 6:')
try:
    wd.find_element(By.LINK_TEXT,'Policies and Code').click()
    time.sleep(3)
    wd.find_element(By.LINK_TEXT,"Policies").click()
    time.sleep(3)
    wd.find_element(By.LINK_TEXT,'Code of Ethics and Conduct').click()
    time.sleep(3)
    print('Success!\n')
except NoSuchElementException:
    print('No New Tab opened. Failed!\n')

# TestCase 7: Programs page
print('TestCase 7:')
try:
    wd.find_element(By.LINK_TEXT,'Student Scholarship Program').click()
    time.sleep(3)
    wd.find_element(By.LINK_TEXT,"Student Mentorship Program").click()
    time.sleep(3)
    wd.find_element(By.LINK_TEXT,'Student SOS Program').click()
    time.sleep(3)
    print('Success!\n')
except NoSuchElementException:
    print('No New Tab opened. Failed!\n')

# TestCase 8: Check the Contact us Page
print("TestCase 8:")
try:
    wd.find_element(By.LINK_TEXT,"Contact Us").click()
    time.sleep(3)
    info = wd.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div[2]/p[2]')
    time.sleep(3)

    # print(info.text)
    if info.text == "+65-8402-8590, info@thesparksfoundation.sg":
        print('Contact Information is Correct!')
    else:
        print('Contact Information is Incorrect!')
    print("Sucessful!\n")
except NoSuchElementException:
    print("Contact Page Verification Unsuccessful!")

# TestCase 9: Links Page
print("TestCase 9:")
try:
    wd.find_element(By.LINK_TEXT,'LINKS').click()
    time.sleep(3)
    wd.find_element(By.LINK_TEXT,'Software & App').click()
    time.sleep(3)
    wd.find_element(By.LINK_TEXT,'AI in Education').click()
    time.sleep(3)
    print('Successful!\n')
except NoSuchElementException:
    print("LINKS Verification Failed!\n")

# TestCase 10: Check the Form
print("TestCase 10:")
try:
    wd.find_element(By.LINK_TEXT,'Join Us').click()
    time.sleep(3)
    wd.find_element(By.LINK_TEXT,'Why Join Us').click()
    time.sleep(3)
    wd.find_element(By.NAME,'Name').send_keys('Anuradha Atole')
    time.sleep(3)
    wd.find_element(By.NAME,'Email').send_keys('anuradhaa2041@gmail.com')
    time.sleep(3)
    select = Select(wd.find_element(By.CLASS_NAME,'form-control'))
    time.sleep(3)
    select.select_by_visible_text('Intern')
    time.sleep(3)
    wd.find_element(By.CLASS_NAME,'button-w3layouts').click()
    time.sleep(3)
    print("Successful!\n")
except NoSuchElementException:
    print("Form Verification Failed!\n")
    time.sleep(3)
cls=wd.close()
