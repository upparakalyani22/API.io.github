import requests
from tabulate import tabulate
import argparse

# Get your own OpenWeatherMap API key
OPENWEATHER_API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"

def define_api_interface():
    print("\n--- Defining API Interface ---")
    print("This demo shows example API calls.")

def remote_api_example():
    print("\n--- Remote API Examples ---")
    # Agify API
    url_age = "https://api.agify.io?name=michael"
    try:
        response = requests.get(url_age, timeout=10)
        response.raise_for_status()
        data = response.json()
        print("\nAgify API Response:")
        print(tabulate(data.items(), headers=["Field", "Value"]))
    except Exception as error:
        print("Error fetching Agify API:", error)

    # CoinGecko API
    url_crypto = "https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=bitcoin"
    try:
        response = requests.get(url_crypto, timeout=10)
        response.raise_for_status()
        crypto_data = response.json()
        print("\nCoinGecko API Response:")
        print(tabulate(crypto_data["bitcoin"].items(), headers=["Currency", "Price"]))
    except Exception as error:
        print("Error fetching CoinGecko API:", error)

    # COVID-19 API
    url_covid = "https://disease.sh/v3/covid-19/all"
    try:
        response = requests.get(url_covid, timeout=10)
        response.raise_for_status()
        covid_data = response.json()
        print(f"\nCOVID-19 Global Cases: {covid_data['cases']:,}, Deaths: {covid_data['deaths']:,}")
    except Exception as error:
        print("Error fetching COVID-19 API:", error)

def api_from_command_line():
    try:
        post_id = int(input("Enter a post ID (1-100): "))
        url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        post = response.json()
        print("\nPost Details:")
        print(tabulate(post.items(), headers=["Field", "Value"]))
    except ValueError:
        print("Invalid input.")
    except Exception as error:
        print("Error fetching post:", error)

def api_limits_example():
    print("\n--- API Limits Example ---")
    max_requests_per_minute = 5
    current_requests = 3
    print(f"Max requests allowed: {max_requests_per_minute}")
    if current_requests < max_requests_per_minute:
        print("You can make more requests.")
    else:
        print("Request limit reached.")

def api_for_js_spa():
    print("\n--- API in JavaScript SPA ---")
    html_content = """
<!DOCTYPE html>
<html>
<head><title>SPA API Demo</title></head>
<body>
    <h2>Bitcoin Price in USD</h2>
    <div id="price">Loading...</div>
    <script>
        fetch('https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=bitcoin')
            .then(response => response.json())
            .then(data => {
                document.getElementById('price').innerText =
                    'Bitcoin Price USD: ' + data.bitcoin.usd;
            })
            .catch(error => {
                document.getElementById('price').innerText = 'Error';
            });
    </script>
</body>
</html>
"""
    with open("spa_api_demo.html", "w", encoding="utf-8") as file:
        file.write(html_content)
    print("SPA demo created: spa_api_demo.html")

if __name__ == "__main__":
    print("\n===== START =====")
    define_api_interface()
    remote_api_example()
    api_from_command_line()
    api_limits_example()
    api_for_js_spa()
    print("\n===== DONE =====")
