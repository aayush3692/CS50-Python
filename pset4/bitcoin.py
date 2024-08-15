import sys
import requests

def main():
    bitcoin_price()

def bitcoin_price():
    try:
       if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")


       n = float(sys.argv[1])

       response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

       data = response.json()

       price = data["bpi"]["USD"]["rate_float"]

       amount = n * price

       print(f"${amount:,.4f}")


    except ValueError:
        sys.exit("Command-line argument is not a number")
    except IndexError:
        sys.exit("Missing command-line argument")
    except requests.RequestException:
        pass




if __name__ == "__main__":
    main()
