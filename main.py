from flask import Flask, Response,jsonify, render_template
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions  # Import for Chrome options
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from bs4 import BeautifulSoup
from replit import db

app = Flask(__name__)


def selenium_task(arg):
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
  driver.get(arg)
  #assert "Jumia Nigeria | Online Shopping for Electronics, Fashion, Home, Beauty & Sport" in driver.title

  page_source = driver.page_source

  driver.close()
  return page_source

product_names = []
product_prices = []
product_old_prices = []
product_images = []
results = {
  "product_names": product_names,
  "product_prices": product_prices,
  "product_old_prices": product_old_prices,
  "product_images": product_images
  
}


@app.route('/get_all/<string:arg>/<int:arg2>')
def selenium_endpoint(arg,arg2):
  

  for i in range(1,arg2):
      page_source = selenium_task(f"https://www.jumia.com.ng/catalog/?q={arg}&page={i}#catalog-listing")
      soup = BeautifulSoup(page_source, features="html.parser")
      data = soup.find('div', class_='-pvs col12')
      name = data.find_all('h3', class_='name')
      price = data.find_all('div', class_='prc')
      Old_price = data.find_all('div', class_='old')
      image = data.find_all('img', class_='img')

      product_names_list = [product_name.text for product_name in name]
      product_price_list = [product_price.text for product_price in price]
      # product_old_price_list = [product_old_price.text for product_old_price in Old_price]
      product_image_list = [img_tag.get('data-src') for img_tag in image]
      #print(product_price_list)
      
      product_names.append(product_names_list)
      product_prices.append(product_price_list)
      # 'product_old_prices': product_old_price_list,
      product_images.append(product_image_list)
  

  return jsonify(results)


@app.route('/discount/<string:arg>/<int:arg2>/<int:arg3>')
def discount(arg,arg2,arg3):
  for i in range(1,arg2):
    page_source = selenium_task(f'https://www.jumia.com.ng/catalog/?q={arg}+&price_discount={arg3}-100&page={arg2}#catalog-listing')
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
    product_names.append(product_names_list)
    product_prices.append(product_price_list)
    product_old_prices.append(product_old_price_list)
    product_images.append(product_image_list)

  return jsonify(results)


@app.route('/')
def index():
  return render_template('index.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0')
keys = db.keys()
keys = db.keys()
