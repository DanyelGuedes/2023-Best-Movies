from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
import random

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)

link = 'https://editorial.rottentomatoes.com/guide/best-movies-of-2023/'
count = 1

driver.get(link)
driver.find_element("xpath", '//*[@id="onetrust-accept-btn-handler"]').click()
sleep(random.randint(2, 6))

while True:
    title = driver.find_element('xpath', f'//*[@id="row-index-{count}"]/div[3]/div[1]/div[1]/div/div/h2/a').text
    nota = driver.find_element('xpath', f'//*[@id="row-index-{count}"]/div[3]/div[1]/div[1]/div/div/h2/span[3]').text
    link = driver.find_element('xpath',f'//*[@id="row-index-{count}"]/div[3]/div[1]/div[1]/div/div/h2/a').get_attribute('href')
    posicao = driver.find_element('xpath', f'//*[@id="row-index-{count}"]/div[3]/div[1]/div[2]/div').text

    print(f'{posicao}º {title} \n Rotten Tomatoes {nota} -- Link {link} \n')
    count += 1

    if count == 21:
        break

driver.quit()