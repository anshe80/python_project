import logging
import sys
import pathlib
import json


class AppReadBase(object):
    def __init__(self, phone_serial, pp):
        self.pp = pp
        self.phone_serial = phone_serial
        self.path = pathlib.Path().cwd()
        self.logger = self.log_config(phone_serial)
        with open(self.path / 'conf' / 'app_info.json', 'r', encoding='UTF-8') as f:
            self.app_info = json.load(f)
        self.package_name = ''

    def app_start(self, app_name):
        app_list_running = self.pp.app_list_running()
        for k, v in self.app_info.items():
            if v[1] == app_name:
                self.package_name = k
                if k in app_list_running:
                    self.pp.app_stop(k)
                self.pp.app_start(k)
                break
        self.logger.error('app名字输入错误，无法启动app')
        raise

    def log_config(self, phone_serial):
        # 设置log
        logger = logging.getLogger(__name__)
        logger.setLevel(level=logging.DEBUG)
        # StreamHandler 输出到控制台的logger
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(level=logging.INFO)
        logger.addHandler(stream_handler)
        # FileHandler 输出到文件的logger
        if not pathlib.Path(self.path / 'log').exists():
            pathlib.Path.mkdir(self.path / 'log')
        file_handler = logging.FileHandler(self.path / 'log' / f'{phone_serial}_log.txt', mode='a', encoding='UTF-8')
        file_handler.setLevel(level=logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s',
                                      datefmt='%Y/%m/%d %H:%M:%S')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger
