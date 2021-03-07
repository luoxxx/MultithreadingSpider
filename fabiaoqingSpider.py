import threading
from queue import Queue
import time
from lxml import etree
import requests
import re
import os

class MyThread(threading.Thread):
    def __init__(self, queue, path):
        threading.Thread.__init__(self)
        self.queue = queue
        self.path = path
        if not os.path.exists(path):
            os.mkdir(path)
    def run(self):
        while True:
            try:
                if not self.queue.empty():
                    url = self.queue.get()
                    download_images(url, self.path)
                    print('下载成功')
                    self.queue.task_done()
                else:
                    break
            except:
                print("下载失败----")



def download_images(url, path):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Mobile Safari/537.36'
    }
    res = etree.HTML(requests.get(url).text)
    urllist = res.xpath('//img[@class="ui image lazy"]/@data-original')
    # print(urllist)
    for u in urllist:
        img = requests.get(u).content
        name = path+u.split(r'/')[-1]
        with open(name, 'wb') as f:
            f.write(img)


if __name__ == '__main__':
    start = time.time()
    _url = 'https://www.fabiaoqing.com/biaoqing/lists/page/{}.html'
    urls = [_url.format(i) for i in range(1, 11)]
    # download_images(url,'./img/')
    queue = Queue()
    for i in urls:
        queue.put(i)
    for i in range(10):
        th01 = MyThread(queue,'./thread02/')
        th01.setDaemon(True)
        th01.start()
    queue.join()
    end = time.time()
    print('执行时间{}'.format(end-start))
    # download_images(url)
'''
    多线程队列 执行时间58.29835915565491
    单线程 执行时间53.94330930709839
'''