import sys
sys.path.append(r"/Users/hanzhiqiang/PycharmProjects/python_test_0/venv/include")


from setting.settingRead import SettingRead
from mysqljdbc import JdbcMysql

if __name__ == "__main__":
    setting = SettingRead("setting.yml")
    jdbcMysql = JdbcMysql(setting.getValue('mysql.host'), setting.getValue('mysql.user'),
                          setting.getValue('mysql.password'), setting.getValue('mysql.db'))
    result = jdbcMysql.select('select * from account')
    print(result)
