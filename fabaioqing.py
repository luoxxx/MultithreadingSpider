import requests
import time
from lxml import etree
import threading
import random

def download_images(url, path):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Mobile Safari/537.36'
    }
    res = etree.HTML(requests.get(url,headers=headers).text)
    urllist = res.xpath('//img[@class="ui image lazy"]/@data-original')
    # print(urllist)
    for u in urllist:
        img = requests.get(u,headers=headers).content
        name = path+u.split(r'/')[-1]
        time.sleep(random.random()*2)
        with open(name, 'wb') as f:
            f.write(img)


if __name__ == '__main__':
    start = time.time()
    _url = 'https://www.fabiaoqing.com/biaoqing/lists/page/{}.html'
    urls = [_url.format(i) for i in range(1, 11)]
    # download_images(url,'./img/')
    queue = []
    for url in urls:
        t = threading.Thread(target=download_images, args=(url, './img/'))
        # t.setDaemon(True)
        t.start()
        queue.append(t)
    for q in queue:
        q.join()
    end = time.time()
    print('执行时间{}'.format(end-start))
    # download_images(url)
'''
    多线程队列 执行时间58.29835915565491
    单线程 执行时间53.94330930709839
'''