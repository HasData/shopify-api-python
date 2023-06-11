Because of its convenience and simplicity, many online stores are built on Shopify. This means that these stores have a similar structure, which facilitates the scraping process.

The Shopify API Python library provides a convenient way to interact with the Shopify Collections API and the Shopify Products API. Using the provided API key. This library lets you get information about collections and products from any Shopify store.

## Features

Our Python Shopify API has some features and benefits:

- Retrieve information about collections in a Shopify store.  
- Fetch detailed product information from a Shopify store. 
- Easily integrate the library into your Python scripts or projects.

## Install

`pip install shopify-python-api`

## API key

To access the Shopify API Python library, you need an API key from Scrape-It.Cloud. Here's how you can obtain the API key:

1. Go to the [Scrape-It.Cloud](https://scrape-it.cloud/) website in your web browser.
2. Sign up for a new account by clicking the "Sign Up" button. 
3. You will also receive some free credits that you can use for API requests. The available credits will be displayed on the dashboard.

After that, you can use your API key in your scrapers.

## Use

To start using the Shopify API library, use this example:

```python
from shopify_api import ShopifyAPI

shopify_api_client = ShopifyAPI("INSERT_YOUR_API_KEY")

try:
	result = shopify_api_client.collections(
		params={
			"url": "https://libertasbella.com/"
		}
	)

	print(result)
except Exception as e:
	print(e.validation_errors)
```

Using this example, you can get Shopify collections. The function has only one required parameter:

- url (required): The URL of the Shopify store.

You can also use our Shopify Python API to get information about products:

```python
from shopify_api import ShopifyAPI

shopify_api_client = ShopifyAPI("INSERT_YOUR_API_KEY")

try:
	result = shopify_api_client.products(
		params={
			"url": "https://libertasbella.com/",
			"limit": 250,
			"page": 1
		}
	)

	print(result)
except Exception as e:
	print(e.validation_errors)
```

Here, in addition to the required parameter, you can also use optional ones to get exactly the data you need:

- limit (optional): The maximum number of products to retrieve. It must be a number between 1 and 250.
- page (optional): The page number of the results to retrieve. It must be a number starting from 1.
- collection (optional): The collection handle to filter the products.

For more detailed information about the response format and parameters, you can go to the [documentation page](https://docs.scrape-it.cloud/shopify-api/).

## How to use Shopify API in Python for Scraping

To use the Shopify API Python library, install it and import it into your Python script.

Use the library functions to get the information you need. For example, you can get collections and products from Shopify by calling the appropriate functions provided by the library.

Remember to replace "YOUR_API_KEY" with the API key you received from Scrape-It.Cloud. Following these steps, you can use the Shopify API Python library to retrieve data from Shopify stores and integrate it into your apps or projects.

You can use our [Shopify no-code scraper](https://scrape-it.cloud/scrapers/shopify) if you don't want to write a script and just need to get information. It allows you to retrieve data from Shopify stores without writing any code.
