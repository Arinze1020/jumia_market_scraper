from flask import Flask, Response
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions  # Import for Chrome options
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from bs4 import BeautifulSoup

app = Flask(__name__)


def selenium_task():
  software_names = [SoftwareName.CHROME.value]

  operating_systems = [
      OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value
  ]

  user_agent_rotator = UserAgent(software_names=software_names,
                                 operating_systems=operating_systems,
                                 limit=10000)
  user_agent = user_agent_rotator.get_random_user_agent()
  options = ChromeOptions()
  options.add_argument(f"user-agent={user_agent}")
  # Change to ChromeOptions
  options.add_argument("--headless")
  options.add_argument("--disable-gpu")
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-dev-shm-usage")
  driver = webdriver.Chrome(options=options)  # Change to webdriver.Chrome

  # Perform the selenium task
  driver.get(
      "https://www.jumia.com.ng/catalog/?q=air+fryer&page=2#catalog-listing")
  #assert "Jumia Nigeria | Online Shopping for Electronics, Fashion, Home, Beauty & Sport" in driver.title

  page_source = driver.page_source

  driver.close()
  return page_source


@app.route('/selenium')
def selenium_endpoint():
  page_source = selenium_task()
  soup = BeautifulSoup(page_source, features="html.parser")
  data = soup.find('div', class_='-pvs col12')
  name = data.find_all('h3', class_='name')
  price = data.find_all('div', class_='prc')
  Old_price = data.find_all('div', class_='old')
  image = data.find_all('img', class_='img')

  product_names_list = [product_name.text for product_name in name]
  product_price_list = [product_price.text for product_price in price]
  product_old_price_list = [
      product_old_price.text for product_old_price in Old_price
  ]
  product_image_list = [img_tag.get('data-src') for img_tag in image]
  print(len(product_names_list))
  print(len(product_price_list))
  #print(len(product_old_price_list))
  print(len(product_image_list))
  return Response(page_source, mimetype='text/html')


@app.route('/discount')
def discount():
  page_source = selenium_task()
  soup = BeautifulSoup(page_source, features="html.parser")
  data = soup.find('div', class_='-pvs col12')
  name = data.find_all('h3', class_='name')
  price = data.find_all('div', class_='prc')
  Old_price = data.find_all('div', class_='old')
  image = data.find_all('img', class_='img')

  product_names_list = [product_name.text for product_name in name]
  product_price_list = [product_price.text for product_price in price]
  product_old_price_list = [
      product_old_price.text for product_old_price in Old_price
  ]
  product_image_list = [img_tag.get('data-src') for img_tag in image]
  print(len(product_names_list))
  print(len(product_price_list))
  print(len(product_old_price_list))
  print(len(product_image_list))
  return Response(page_source, mimetype='text/html')


@app.route('/')
def index():
  return "200 OK"


if __name__ == '__main__':
  app.run(host='0.0.0.0')
