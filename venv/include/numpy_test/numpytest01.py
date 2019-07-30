import requests
import json
import time
import simplejson

headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0'
}
base_url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=38975978198&spuId=279689783&sellerId=92889104&order=3&callback=jsonp698'


for i in range(2, 98, 1):
    url = base_url + '&currentPage=%s' % str(i)
    tb_req = requests.get(base_url, headers=headers).text[13:-1]
    tb_dict = simplejson.loads(tb_req)
    tb_json = json.dumps(tb_dict, indent=2)
    review_j = json.loads(tb_json)
    print("获取的URL为：%s" % review_j['url'])
    time.sleep(1)
