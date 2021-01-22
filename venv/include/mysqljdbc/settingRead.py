# pip install PyYaml
import yaml


class SettingRead:
    def __init__(self, path):
        with open(path) as setTing:
            self.settingYaml = yaml.load(setTing)

    def getValue(self, key):
        print(self.settingYaml)
        tmpData = self.settingYaml
        for tmp in key.split('.'):
            tmpData = tmpData[tmp]
        return tmpData


if __name__ == '__main__':
    setting = SettingRead("../mysqljdbc/setting.yml")
    print(setting.getValue("mysql.host"))


