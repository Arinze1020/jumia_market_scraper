
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![Replit Badge](https://img.shields.io/badge/Replit-Blue?style=flat&logo=Replit&logoColor=Blue)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](code-of-conduct.md)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Build status](https://ci.appveyor.com/api/projects/status/pjxh5g91jpbh7t84?svg=true)](https://ci.appveyor.com/project/tygerbytes/resourcefitness)
 [![Coverage Status](https://coveralls.io/repos/github/leonkoech/Jumia-Python-Web-Scraper/badge.svg?branch=master)](https://coveralls.io/github/leonkoech/Jumia-Python-Web-Scraper?branch=master)



# Jumia_API-like Data Scraping with Selenium and Flask

> Bot must follow this rules
 Site scaping is permited IF the user-agent is clearly identify it as a bot and
the bot owner and is using less than 200 request per minute
Bot identification must have a owner url or contact if we need to contact them
Bots with fake user-agent will be blocked
Bots trying to use too many IPs to increase performance may also be blocked.
If you need more than 200 RPM, please contact the email techops at jumia com [jumia robots.txt](https://www.jumia.com.ng/robots.txt)



This project involves building an API that can scrape data from a specific webpage, similar to how the Jumia website is scraped for product information. It utilizes the Selenium library for web scraping and the Flask microframework for building the API.

# How it Works:

### Web Scraping with Selenium:

- Selenium is used to automate the process of opening a web browser, navigating to the desired webpage (e.g., a Jumia search results page), and extracting the necessary data.

### Flask:

- Flask is used to create an API endpoint that allows external applications to access the scraped data.
- The API endpoint can be called with specific parameters, such as the search query or product category, to retrieve the relevant data.

### Valuable Information Retrieved:

The data scraped from the Jumia search results page typically includes the following valuable information:

- Product title

- Product price

- Product image URL

- Product rating



### Example Usage:

To use the API, a client application can make a request to the API endpoint with the desired parameters. For instance, to scrape data for products related to "mobile phones," the client application would send a request to the endpoint with the search query "mobile phones."

Upon receiving the request, the API would invoke Selenium to scrape the Jumia search results page and extract the relevant product information. This information would then be returned to the client application in a structured format, such as JSON.

# Requirements
This package requires the following to run:

- [python](https://www.python.org/downloads/)>=3.11

# Installation
First you have to clone the repo by writing the following code

 `Clone the git rep`

Change directory to jumia python web scraper
 `cd in to the repo or open it with a text editor. Because that's where the main python file is (main.py)`
 `Activate your Virtual Environment (venv)`

Then run 

`pip install -r requirements.txt`
# Usage
Then run the python file

`python main.py`

<h2>Endpoints:</h2>
      <ul>
          <li><strong>GET /</strong> - Homepage (This page)</li>
          <li><strong>GET /product_name/{number_of_page}</strong> - Scrapes products from Jumia based on page number</li>
          <li><strong>GET /product_name/{discount_percentage}/{number_of_page}</strong> - Scrapes products with a discount percentage from Jumia based on page number</li>

# Contribution
You can contribute to this project.
To contribute to this project, clone repo locally and commit your code on a seperate branch.
 
You can also reach me via [email](arinzeugwuanyi@gmail.com) me or better yet, shoot me a [twitter](https://twitter.com/ArinzeUgwuanyi) DM.

# license
[MIT](#) license.  
