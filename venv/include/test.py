from setting.settingRead import SettingRead

if __name__ == '__main__':
    setting = SettingRead("./mysqljdbc/setting.yml")
    print(setting.getValue("mysql.host"))
