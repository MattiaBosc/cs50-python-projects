# Bitcoin Price Index

**Description:**  
`bitcoin.py` queries the CoinCap v3 API to retrieve the current Bitcoin price and calculates the total cost for a specified number of Bitcoins.

**Behavior:**
1. Expects the user to provide the number of Bitcoins as a command-line argument.  
   - If missing, exits with an error: `Missing command-line argument`.  
   - If not a number, exits with an error: `Command-line argument is not a number`.
2. Queries the CoinCap v3 API at: `https://rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey`.
   - Replace `YourApiKey` with your actual API key.
3. Retrieves the current Bitcoin price (USD) from the JSON response.
4. Outputs the total cost for the specified number of Bitcoins:
   - Formatted to **four decimal places**.
   - Uses a **comma as thousands separator**.
