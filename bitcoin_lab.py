import requests


def main():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    usd_conversion = api_call(url)
    bitcoin = get_bitcoin_holdings()
    bitcoin_value_in_dollars = conversion_equation(usd_conversion, bitcoin)
    display_conversion_info(usd_conversion)
    display_result(usd_conversion, bitcoin, bitcoin_value_in_dollars)


# this function calls the API and gets the information we need. It returns a dictionary with the conversion information
# 'description' included in case we want to expand program to include other currencies
def api_call(url):
    results = requests.get(url).json()
    usd_info = results['bpi']['USD']
    # description = usd_info['description']
    usd_conversion = usd_info['rate_float']

    return usd_conversion


# asks user how many bitcoins they have
def get_bitcoin_holdings():
    while True:
        try:
            bitcoin = float(input('Enter number bitcoins you have: '))
            if bitcoin <= 0:
                raise ValueError('Bitcoin value must be greater than zero.')
            return bitcoin
        except:
            print('Enter value greater than zero')


# simple math converts bitcoin holdings to usd at current values
def conversion_equation(usd_conversion, bitcoin):
    return bitcoin * usd_conversion

# displays info about conversion
def display_conversion_info(usd_conversion):
    print(f'Currently 1 bitcoin is worth {usd_conversion}')

# displays info to user in helpful way
def display_result(bitcoin, bitcoin_value_in_dollars):
    print(f'{bitcoin} Bitcoin is equivalent to ${bitcoin_value_in_dollars:.2f}')


if __name__ == '__main__':
    main()
