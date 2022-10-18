// pch.cpp: 与预编译标头对应的源文件

#include "pch.h"

int SetWallPaper(char* pic_path)
{
	return SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, (PVOID)pic_path, SPIF_UPDATEINIFILE);
}

// 当使用预编译的头时，需要使用此源文件，编译才能成功。
