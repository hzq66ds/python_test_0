import os  # Python的标准库中的os模块包含普遍的操作系统功能
import re  # 引入正则表达式对象
import urllib  # 用于对URL进行编解码
from http.server import HTTPServer, BaseHTTPRequestHandler  # 导入HTTP处理相关的模块


# 将当前目录http： python -m http.server 8888 &
# 搜索8888端口占用： lsof -i tcp:8888

# 自定义处理程序，用于处理HTTP请求
class TestHTTPHandler(BaseHTTPRequestHandler):
    # 处理GET请求
    def __init__(self, request: bytes, client_address: Tuple[str, int], server: socketserver.BaseServer):
        super().__init__(request, client_address, server)
        self.protocal_version = 'HTTP/1.1'  # 设置协议版本

    def do_GET(self):
        # 页面输出模板字符串
        templateStr = '''  
            <html>  
            <head>  
            <title>QR Link Generator</title>  
            </head>  
            <body>  
            %s
            <br>  
            <br>  
            <form action="/qr" name=f method="GET">
                <input maxLength=1024 size=70 name=s value="" title="Text to QR Encode"><input type=submit value="Show QR" name=qr>  
            </form>
            </body>  
            </html> '''

        # 将正则表达式编译成Pattern对象
        pattern = re.compile(r'/qr\?s=([^\&]+)\&qr=Show\+QR')
        # 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
        match = pattern.match(self.path)
        qrImg = ''

        if match:
            # 使用Match获得分组信息
            qrImg = '<img src="http://chart.apis.google.com/chart?chs=300x300&cht=qr&choe=UTF-8&chl=' + match.group(1) \
                    + '" /><br />' + urllib.unquote(match.group(1))

        self.send_response(200)  # 设置响应状态码
        self.send_header("Welcome", "Contect")  # 设置响应头
        self.end_headers()
        self.wfile.write(bytes(templateStr % qrImg, encoding="utf8"))  # 输出响应内容


# 启动服务函数
def start_server(port):
    http_server = HTTPServer(('', int(port)), TestHTTPHandler)
    http_server.serve_forever()  # 设置一直监听并接收请求


start_server(8000)  # 启动服务，监听8000端口
