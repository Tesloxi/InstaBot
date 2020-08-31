from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import time

try:
    f = open("./logs.txt", "r")
except FileNotFoundError:
    username = input('Your username : ')
    password = input('Your password : ')
    f = open('./logs.txt', 'a')
    f.write(username + '\n')
    f.write(password)
    f.close()
finally:
    f = open("./logs.txt", "r")
    username = f.readline()
    password = f.readline()
    f.close()

message_to = input('Enter the username of the person you want to send a message to : ')
message = input('Enter your message : ')

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://instagram.com/" + message_to)

header = driver.find_elements_by_tag_name("header")
if header: 
    button = driver.find_element_by_link_text("Se connecter")
    button.click()
    try:
        username_field = WebDriverWait(driver, 10).until(
            Ec.presence_of_element_located((By.NAME, "username"))
        )
        username_field.send_keys(username)

        password_field = driver.find_element_by_name("password")
        password_field.send_keys(password)

        connexion_button = driver.find_element_by_css_selector("button.sqdOP.L3NKy.y3zKF")
        connexion_button.click()

        div = WebDriverWait(driver, 10).until(
            Ec.presence_of_element_located((By.CSS_SELECTOR, "div.cmbtv"))
        )
        later = div.find_element_by_tag_name("button")
        later.click()

        contact_button = WebDriverWait(driver, 10).until(
            Ec.presence_of_element_located((By.CSS_SELECTOR, "button.fAR91.sqdOP.L3NKy._4pI4F._8A5w5"))
        )
        contact_button.click()

        div = WebDriverWait(driver, 10).until(
            Ec.presence_of_element_located((By.CSS_SELECTOR, "div.mt3GC"))
        )
        later = div.find_element_by_class_name("HoLwm")
        later.click()

        textarea = driver.find_element_by_tag_name("textarea")
        textarea.send_keys(message)
        textarea.send_keys(Keys.RETURN)

        time.sleep(2)
        driver.quit()

    except:
        print('Cannot contact this person')
else:
    print("Can't find the username you entered")
    driver.quit()