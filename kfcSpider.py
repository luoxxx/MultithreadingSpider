'''
    kfc爬取
'''
import requests
import json
import time
import random
def spider_kfc(url, addr, page=1):
    param = {
        "cname": "",
        "pid": "",
        "keyword": addr,
        "pageIndex": str(page),
        "pageSize": "10"
    }
    header={
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Mobile Safari/537.36'
    }

    res = requests.post(url, headers=header, params=param)
    res = json.loads(res.text)["Table1"]
    if res:
        for r in res:
            print(r['addressDetail'])
        spider_kfc(url, addr, page + 1)
        time.sleep(random.random()*4)
    else:
        return

if __name__ == '__main__':
    # addr = input("输入需要查询的地点/关键字：")
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    spider_kfc(url, "深圳北站A区二楼")