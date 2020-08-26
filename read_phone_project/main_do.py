from multiprocessing import Process
from phone_connect import PhoneConnect
from app_jiao_ben.qu_tou_tiao import QuTouTiao
import uiautomator2
import random


def main_run(phone_serial):
    pp = uiautomator2.connect_usb(phone_serial)
    pp.unlock()
    # 禁用USB充电
    pp.shell('dumpsys battery set usb 0')
    # 设置电池电量
    pp.shell(f'dumpsys battery set level {random.randint(15, 95)}')
    # 设置电池为非充电状态
    pp.shell('dumpsys battery set status 1')
    # 查看电池状态
    # print(pp.shell('dumpsys battery').output)

    print(pp.shell(f'settings get secure location_providers_allowed').output)
    QuTouTiao(phone_serial, pp).main_do()
    # 设置电池为充电状态
    # pp.shell('dumpsys battery set status 2')
    # 重置电池状态
    pp.shell('dumpsys battery reset')


if __name__ == '__main__':
    process_job_list = []
    phone_list = PhoneConnect().serials
    for serial in phone_list:
        p1 = Process(target=main_run, args=(serial,))
        p1.start()
        process_job_list.append(p1)
    for j in process_job_list:
        j.join()

