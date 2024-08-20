import os
from configparser import ConfigParser

filepath = os.path.join(os.path.dirname(__file__), 'configfile.ini')


class MyParser(ConfigParser):

    def optionxform(self, optionstr):
        return optionstr

    def toDict(self):
        return dict(self._sections)


def get_conf():
    myParser = MyParser(defaults=None)
    if os.path.isfile(filepath):
        try:
            myParser.read(filenames=filepath, encoding='UTF-8')
            result = myParser.toDict()
            return result
        except OSError:
            raise ValueError("Read config failed:%s"%OSError)


def get_log_config():
    return get_conf()['log']


def get_idcard_config():
    return get_conf()['idcard']


def get_report_config():
    return get_conf()['report']


def get_cases_config():
    return get_conf()['cases']


if __name__ == '__main__':

    print(get_idcard_config()['IDcard_upload_path'])


