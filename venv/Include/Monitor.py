from Include.GlobalValues import url,sleep_times
import json,requests,datetime,time
def price_monitor(price):
    global sleep_times,url
    while True:
        p = price.get()
        res = json.loads(requests.get(url=url).text)
        if(res['status'].strip() == 'success'):
            for i in res['data']['prices']:
                if p == 0:
                    price.put(float(i['price']))
                else:
                    price.put((p + float(i['price'])) / 2)
        print(datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))
        print(p)
        time.sleep(sleep_times)