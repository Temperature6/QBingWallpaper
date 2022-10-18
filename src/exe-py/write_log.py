import time
import os
log_dir = ".\\Log"
log_path = log_dir + "\\WallPaper_{0}.log"


def GetCurrentTimeStr():
    return time.strftime("[%Y/%m/%d-%H:%M:%S]", time.localtime())


def GetDateStr():
    return time.strftime("%Y%m%d", time.localtime())


def WriteLog(log_str):
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    log_file = open(log_path.format(GetDateStr()), "a+")
    log_file.write(GetCurrentTimeStr() + log_str + "\n")
    log_file.close()


if __name__ == "__main__":
    WriteLog("123")
