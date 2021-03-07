'''
    Tencent招聘
    Request URL: https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1614773748869&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=40001&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn
'''
import time
import requests
import json
import random
import threading
from writeExcel import SaveExcel
url = 'https://careers.tencent.com/tencentcareer/api/post/Query?'

NUM = 0
def parse(url, num, lock):
    # global NUM
    header = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Mobile Safari/537.36"
    }
    param = {
        "timestamp": int(time.time()*1000),
        "countryId": "",
        "cityId": "",
        "bgIds": "",
        "productId": "",
        "categoryId": "",
        "parentCategoryId": "",
        "attrId": "",
        "keyword": "",
        "pageIndex": str(num),
        "pageSize": "10",
        "language": "zh-cn",
        "area": "cn"
    }
    res = requests.get(url, headers=header, params=param)
    res = json.loads(res.text)["Data"]["Posts"]
    # print(res)
    # excels = SaveExcel()
    lock.acquire()
    with open('tencent2.txt', 'a+', encoding='utf-8') as f:
        for r in res:
            CategoryName = r['CategoryName']
            RecruitPostName = r['RecruitPostName']
            Responsibility = r['Responsibility']
            LastUpdateTime = r['LastUpdateTime']
            LocationName = r['LocationName']
            ls = [CategoryName, RecruitPostName, Responsibility, LastUpdateTime, LocationName]
            print(ls)
            json.dump(ls, f, ensure_ascii=False)
            f.write('\n')
    lock.release()
# if __name__ == '__main__':
#     start = time.time()
#     # parse(url, 2)
#     for i in range(1, 392):
#         parse(url, i)
#         time.sleep(random.random()*3)
#     end = time.time()
#     print("执行时间：{}".format(end-start))

if __name__ == '__main__':
    start = time.time()
    # parse(url, 2)
    lock = threading.Lock()
    th = []
    for i in range(1, 392):
        th.append(threading.Thread(target=parse, args=(url, i, lock)))
        time.sleep(random.random() * 3)
    for t in th:
        t.start()
    for t in th:
        t.join()
    end = time.time()
    print("执行时间：{}".format(end-start))


'''
单线程执行时间 724.8186104297638   805.3839445114136
多线程执行时间 621.5665860176086   627.1867587566376
'''
