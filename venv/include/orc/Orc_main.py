# -*- coding: utf-8 -*-
import requests
import base64
import sys

sys.path.append(r"/Users/hanzhiqiang/PycharmProjects/python_test_0/venv/include")
from setting.settingRead import SettingRead


class Orc_main:
    def __init__(self, grant_type, client_id, client_secret):
        tokenUrl = "https://aip.baidubce.com/oauth/2.0/token"
        data = {
            'grant_type': grant_type,
            'client_id': client_id,
            'client_secret': client_secret
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        resultToken = requests.post(tokenUrl, params=headers, data=data).json()
        self.access_token = resultToken['access_token']

    def orc_look(self, imgPath):
        access_token = self.access_token
        # 自行注册百度云账号，即可获取自己专属的access_token，必须输入！
        with open(imgPath, 'rb') as f:
            image_data = f.read()
            base64_ima = base64.b64encode(image_data)
            data = {
                'image': base64_ima
            }
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=" + str(access_token)
            r = requests.post(url, params=headers, data=data).json()
            print("百度ocr返回结果%s" % r)
            for word in r['words_result']:
                yield word['words']
            # 返回一个生成器，可自行修改


if __name__ == '__main__':
    setting = SettingRead('setting.yml')
    om = Orc_main(setting.getValue('baidu.ocr.grant_type'),
                  setting.getValue('baidu.ocr.client_id'),
                  setting.getValue('baidu.ocr.client_secret'))
    path = "verifyCode.png"  # 图片文件路径，必须输入！
    words = om.orc_look(path)
    # 输出文字(返回结果)
    for word in words:
        print(word)
