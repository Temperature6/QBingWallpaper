from ctypes import *

dll = CDLL("WPChanger.dll")


def SetWP(pic_path):
    return dll.SetWallPaper(pic_path.encode())


if __name__ == "__main__":
    print(SetWP("D:\\Python\\PyProj\\BingWP\\wallpaper.png"))
