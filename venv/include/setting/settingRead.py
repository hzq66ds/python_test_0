# pip install PyYaml
import yaml


class SettingRead:
    def __init__(self, path):
        with open(path) as setTing:
            self.settingYaml = yaml.load(setTing)

    def getValue(self, key):
        tmpData = self.settingYaml
        for tmp in key.split('.'):
            tmpData = tmpData[tmp]
        return tmpData



