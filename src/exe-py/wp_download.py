import os
import requests
import time
from public_val import *
from write_log import *


def GetTime():
    return time.strftime("%Y%m%d", time.localtime())


def DownloadWallPaper(time_str):
    try:
        last_time = time.time()
        rqs = requests.get("https://bingwallpaperimages.azureedge.net/hpimages/Latest/3840x2160/{0}.jpg".format(time_str))
        if rqs.status_code == 200:
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            save_ = "{0}\\{1}.jpg".format(save_dir, time_str)
            pic_file = open(save_, "wb")
            pic_file.write(rqs.content)
            current_time = time.time()
            WriteLog("[Success]Download \"{0}\" in {1} seconds".format(os.path.abspath(save_), (round(current_time - last_time, 2))))
        else:
            WriteLog("[Fail]Fail to get picture from server, status code is {0}".format(rqs.status_code))
        return
    except requests.ConnectionError:
        WriteLog("Fail to Connect")
        return


if __name__ == "__main__":
    DownloadWallPaper("20221011")
    pass
