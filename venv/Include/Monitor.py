from Include.GlobalValues import BTCUrl, sleep_times
import json, requests, datetime, time
from Include.GlobalValues import price

def price_monitor():
    while True:
        update_price(json.loads(requests.get(url=BTCUrl).text))
        print_log();
        time.sleep(sleep_times)


def update_price(result):
    if (result['status'].strip() == 'success'):
        price.put(calculate_price(result['data']['prices']))


def calculate_price(prices):
    base_price = 0
    for one_of_princes in prices:
        if base_price == 0:
            base_price = float(one_of_princes['price'])
        else:
            base_price = (base_price + float(one_of_princes['price'])) / 2
    return base_price


def print_log():
    print(datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))
    print(price.get())