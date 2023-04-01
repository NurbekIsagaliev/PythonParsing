from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import xml.etree.ElementTree as ET

options = Options()
options.add_argument('--headless')  
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
driver_path = '/path/to/chromedriver'  
service = Service(driver_path)

driver = webdriver.Chrome(service=service, options=options)

url = "https://stopgame.ru/news/all/p1"
driver.get(url)


products = driver.find_elements(By.CSS_SELECTOR, '.item.article-summary')


root = ET.Element('Игровые новости')

for product in products:
    name = product.find_element(By.CSS_SELECTOR, 'div.caption.caption-bold').text.strip()
    info = product.find_element(By.CSS_SELECTOR, 'div.info').text.strip()

    product_elem = ET.Element('Игровая новость')
    name_elem = ET.Element('Имя')
    info_elem = ET.Element('Элемент')

    name_elem.text = name
    info_elem.text = info

    product_elem.append(name_elem)
    product_elem.append(info_elem)
    
    root.append(product_elem)

tree = ET.ElementTree(root)
tree.write('products.xml', encoding='utf-8', xml_declaration=True)

driver.quit()
