import requests
from bs4 import BeautifulSoup
import pandas
import time
import threadpool
import threading


class mythread(threading.Thread):
    def __init__(self, id, url):
        threading.Thread.__init__(self)
        self.id = id
        self.url = url

    def run(self):
        print(self.id, self.url)


def getdata(url):
    print('url:    ', url)
    return requests.get(url, headers=getheaders())


# 头信息伪装
def getheaders():
    return {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}


def getcsv(dt, cvsdata):
    dataresult = []
    tmp_img = dt.find('a')
    min_data = getdata(url + tmp_img.get('href')).text
    min_sop = BeautifulSoup(min_data, 'lxml')
    print(dt.find('a').get_text())
    numpage = 1
    while True:
        if numpage > 10:
            break
        try:
            rmi = min_sop.find('div', {'class': 'detail_right_div'}).find_all('li')
            for m in list(rmi):
                print(m.find('a').get('href'))
                rmi_data = getdata(url + m.find('a').get('href')).text
                title = m.find('img').get('title')
                div = BeautifulSoup(rmi_data, 'lxml').find('div', {'class': 'dz'})
                if div is not None:
                    url_tmp = div.find('p').get_text()
                    dataresult.append(title + '        ' + url_tmp)
                else:
                    continue
            nextbutt = min_sop.find('a', {'class': 'pagelink_a'})
            if nextbutt is not None:
                min_sop = BeautifulSoup(getdata(url + nextbutt.get('href')).text, 'lxml')
            else:
                break
        except OSError as e:
            continue
        numpage += 1

    if len(dataresult) > 0:
        cvsdata[tmp_img.get_text()] = dataresult
        cvsdata.to_csv(dt.find('a').get_text() + '.csv', index=None)


if __name__ == '__main__':
    url = 'http://www.henhenlu.org/'
    data = getdata(url)
    sop = BeautifulSoup(data.text, 'lxml')
    books = sop.find('ol', {'class': 'block'})

    cvsdata = pandas.DataFrame()
    a = 0
    for dt in list(books.find_all('li')):
        try:
            if dt.find('a').get_text() == '首页':
                continue
            if a == 0:
                getcsv(dt, cvsdata)
                a += 1
        except OSError as e:
            continue




