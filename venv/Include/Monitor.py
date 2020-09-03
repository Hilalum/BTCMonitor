from Include.GlobalValues import price,url,sleep_times
import json,requests,datetime,time
def price_monitor():
    global price,sleep_times,url
    while True:
        res = json.loads(requests.get(url=url).text)
        if(res['status'].strip() == 'success'):
            for i in res['data']['prices']:
                if price == 0:
                    price = float(i['price'])
                else:
                    price = (price + float(i['price'])) / 2
        print(datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))
        print(price)
        time.sleep(sleep_times)