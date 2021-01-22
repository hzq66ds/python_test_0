from urllib.request import urlopen
import smtplib
from datetime import date
import zlib


for line in urlopen('https://cloud.baidu.com/doc/OCR/s/Ek3h7xypm'):
    line = line.decode('utf-8')  # Decoding the binary data to text.
    print(line)


now = date.today()
print(now)