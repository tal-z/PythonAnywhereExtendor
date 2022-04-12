
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

load_dotenv()

# Instantiate browser session with custom options, removing automation flags in chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument("--disable-gpu")


def renew_task(user_varname: str, password_varname: str):
    try:
        driver = webdriver.Chrome(ChromeDriverManager(version="90.0.4430.24").install(), options=options)
    except:
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # Log into Python Anywhere
    driver.get("https://www.pythonanywhere.com/login/")
    username = driver.find_element(by=By.ID, value="id_auth-username")
    pwd = driver.find_element(by=By.ID, value="id_auth-password")
    nxt = driver.find_element(by=By.ID, value="id_next")
    username.send_keys(os.getenv(user_varname))
    pwd.send_keys(os.getenv(password_varname))
    nxt.click()

    # Navigate to tasks tab
    driver.get("https://www.pythonanywhere.com/user/talzakenautorenew/tasks_tab/")
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
        "/html/body/div[1]/div[2]/div[2]/div[3]/div/div/table/tbody/tr/td[6]/button[4]"))
    ).click()
    driver.close()


def renew_webapp(user_varname: str, password_varname: str):
    try:
        driver = webdriver.Chrome(ChromeDriverManager(version="90.0.4430.24").install(), options=options)
    except:
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # Log into Python Anywhere
    driver.get("https://www.pythonanywhere.com/login/")
    username = driver.find_element(by=By.ID, value="id_auth-username")
    pwd = driver.find_element(by=By.ID, value="id_auth-password")
    nxt = driver.find_element(by=By.ID, value="id_next")
    username.send_keys(os.getenv(user_varname))
    pwd.send_keys(os.getenv(password_varname))
    nxt.click()

    # Navigate to web tab
    driver.get("https://www.pythonanywhere.com/user/talzaken/webapps/#tab_id_talzaken_pythonanywhere_com")

    # click extend button
    extend_button = driver.find_element(by=By.CLASS_NAME, value='webapp_extend')
    extend_button.click()
    driver.close()

if __name__ == '__main__':
    renew_task('PA_renew_username', 'PA_renew_password')
    renew_webapp('PA_username', 'PA_password')


