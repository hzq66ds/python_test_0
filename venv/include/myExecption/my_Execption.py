import os
import shutil
import glob

class MyException0(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

try:
    raise MyException0(2)
except MyException0 as e:
    print("a",e.__str__())

print(os.getcwd())
os.system('mkdir today')

shutil.copyfile("", "")