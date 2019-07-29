from urllib.request import urlopen
import smtplib
from datetime import date
import zlib


for line in urlopen('https://mp.weixin.qq.com/s/uWm-2umIR0UBmaldmY7i3w'):
    line = line.decode('utf-8')  # Decoding the binary data to text.
    print(line)


now = date.today()
print(now)