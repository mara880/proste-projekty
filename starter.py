from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from time import sleep

private = webdriver.ChromeOptions()
private.add_argument("--incognito")
private.add_argument("--start-maximized")

driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=private)


def read_site():
    data = pd.read_excel("config.xlsx")
    counter = 0
    number_of_row = data["Strony"].size
    tablicax = []
    while counter < number_of_row:
        asd = data["Strony"].loc[counter]
        counter += 1
        tablicax.append(asd)
    return tablicax

def start():
    number_of_sites = pd.read_excel("config.xlsx")["Strony"].size-1
    counter = 0
    i = 0
    while number_of_sites >= counter:
        i += 1
        site = (read_site()[counter])
        driver.get(site)
        sleep(2)
        if i <= number_of_sites:
            driver.execute_script('window.open()')
            driver.switch_to.window(driver.window_handles[i])
        counter += 1

start()


