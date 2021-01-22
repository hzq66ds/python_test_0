# -*- coding: utf-8 -*-
import requests
import base64


class Orc_main:
    def getToken(self):
        tokenUrl = "https://aip.baidubce.com/oauth/2.0/token"
        data = {
            'grant_type': 'client_credentials',
            'client_id': '66HRzdfYGGRAg4c5U87sW1W7',
            'client_secret': 'M1X2wXaVrGNA963d2EwtyUHIf4WmBOuM'
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        url = tokenUrl
        r = requests.post(url, params=headers, data=data).json()
        print("百度ocr返回结果%s" % r)
        return r

    def orc_look(self, path):
        access_token = self.getToken()['access_token']
        # 自行注册百度云账号，即可获取自己专属的access_token，必须输入！
        with open(path, 'rb') as f:
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
    om = Orc_main()
    path = "verifyCode.png"  # 图片文件路径，必须输入！
    words = om.orc_look(path)
    # 输出文字(返回结果)
    for word in words:
        print(word)
