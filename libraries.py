# A library is a pre-writtem Python code that solves common problems.
# API- Application Programming Interface
# It is a way a program talks to another program


# import requests

# url = "https://api.coindesk.com/v1/bpi/currentprice.json"

# response = requests.get(url)

# print("Status Code:", respomse.status_code)

# data = response.json()

# print(data)



# import requests

# url = "https://api.coindesk.com/v1/bpi/currentprice.json"

# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()

#     price = data["bpi"]["USD"]["rate"]

#     price("Current Bitcoin Price (USD): ", price)
# else:
#     print("Failed to retrieve data.")


# import requests
# import matplotlib.pyplot as plt

# url = "https://api.coindesk.com/v1/bpi/currentprice.json"

# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
#     price = data["bitcoin"]["usd"]
#     print("Bitcoin Price(USD):", price)
# else:
#     print("Failed with status code:", response.status_code)

# except requests.exceptions.RequestException as e:
#     print("Network error", e)



# import matplotlib.pyplot as plt
# # matplotlib is the full library
# # pyplot is a module inside matplotlib used for plotting
# # plt creates a shorter nickname for plot

# days = ["Mon", "Tue","Wed", "Thu", "Fri"]
# prices = [40000, 41000, 42000, 43000, 43000]

# plt.plot(days, prices)

# plt.title("Bitcoin Price over Time")
# plt.xlabel("Days") #Days are on the x axis
# plt.ylabel("Price") # Price are on the y axis

# plt.show()


import requests
import matplotlib.pyplot as plt

# Step 1: Define API URL
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

try:
    # Step 2: Send request to API
    response = requests.get(url)

    # Step 3: Check if request was successful
    if response.status_code == 200:
        data = response.json()

        # Step 4: Extract useful data
        price = data["bitcoin"]["usd"]

        print("Current Bitcoin Price (USD):", price)

        # Step 5: Create sample historical data
        prices = [price - 800, price - 400, price - 200, price]
        days = ["3 Days Ago", "2 Days Ago", "Yesterday", "Today"]

        # Step 6: Plot the data
        plt.plot(days, prices)
        plt.title("Bitcoin Price Trend")
        plt.xlabel("Days")
        plt.ylabel("Price (USD)")
        plt.show()

    else:
        print("Error: API returned status code", response.status_code)

except requests.exceptions.RequestException as e:
    print("Network error occurred:", e)
