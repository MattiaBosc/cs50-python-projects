import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Provide one command-line argument")

try:
    number = float(sys.argv[1])
except:
    sys.exit("Command-line argument must be a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("API not available")
else:
    response = response.json()
    rate_float = response["bpi"]["USD"]["rate_float"]

print(f"${number*rate_float:,.4f}")
