import sys
sys.path.append(r"/Users/hanzhiqiang/PycharmProjects/python_test_0/venv/include")
from setting.settingRead import SettingRead
from ElasticJdbc import EsJdbc

if __name__ == '__main__':
    setting = SettingRead("setting.yml")
    esjdbc = EsJdbc(setting.getValue('es.host'), setting.getValue('es.port'),
                    setting.getValue('es.username'), setting.getValue('es.password'))

    print(esjdbc.search("test0"))



