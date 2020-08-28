def timer(n):
    while True:
        url = "https://sochain.com/api/v2/get_price/BTC/USD"
        res = json.loads(requests.get(url=url).text)
        if(res['status'].strip() == 'success'):
            for i in res['data']['prices']:
                if price == 0:
                    price = float(i['price'])
                else:
                    price = (price + float(i['price'])) / 2
        print(datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))
        print(price)
        time.sleep(n)