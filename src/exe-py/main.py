import sys

import schedule

from wp_download import *
from dllfunc import *


def DeleteOldWP():
    """
    删除5~10天前的旧壁纸
    :return: 无
    """
    time_now = time.time()
    for i in range(-10, -5):
        time_struct = time.localtime(time_now + i * 86400)
        time_str = time.strftime("%Y%m%d", time_struct)
        file = "{0}\\{1}.jpg".format(save_dir, time_str)
        if os.path.exists(file):
            os.remove(file)
            WriteLog(f"Delete Old Wallpaper:\"{os.path.abspath(file)}\"")
        else:
            continue


def DownloadWP():
    """
    下载0~5天前的壁纸
    :return: 无
    """
    time_now = time.time()
    for i in range(-5, 1):
        time_struct = time.localtime(time_now + i * 86400)
        time_str = time.strftime("%Y%m%d", time_struct)
        if os.path.exists("{0}\\{1}.jpg".format(save_dir, time_str)):
            continue
        DownloadWallPaper(time_str)


def ChangeTodayWP():
    time_now = time.time()
    for i in range(5):
        time_struct = time.localtime(time_now - i * 86400)
        time_str = time.strftime("%Y%m%d", time_struct)
        file = os.path.abspath("{0}\\{1}.jpg".format(save_dir, time_str))
        if os.path.exists(file):
            if not os.path.exists(".\\CWP.txt"):
                f = open(".\\CWP.txt", "a+")
                f.close()
            cwp = open(".\\CWP.txt", "r+")
            data = cwp.read()
            if data == time_str:
                cwp.close()
                return
            SetWP(file)
            cwp.seek(0)
            cwp.truncate()
            cwp.write(time_str)
            cwp.close()
            WriteLog(f"Set WallPaper:\"{file}\"")
            return


def WorkCircle():
    WriteLog("Do Work Circle.....")
    DeleteOldWP()
    DownloadWP()
    ChangeTodayWP()


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        os.chdir(sys.argv[1])
    WriteLog("Running...")
    WorkCircle()
    schedule.every().hour.do(WorkCircle)
    while True:
        schedule.run_pending()
        time.sleep(500)


