#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os 

os.system("clear");
print("                                     o8o             ooooo      ooo");
print("                                     `\"\'             `888b.     `8\'");
print("            oooo    ooo ooo. .oo.   oooo   .oooooooo  8 `88b.    8");
print("             `88b..8P'  `888P\"Y88b  `888  888' `88b   8   `88b.  8 ");
print("               Y888'     888   888   888  888   888   8     `88b.8 ");
print("             .o8\"'88b    888   888   888  `88bod8P'   8       `888 ");
print("            o88'   888o o888o o888o o888o `8oooooo.  o8o        `8 ");
print("                                          d\"     YD                ");
print("                                          \"Y88888P'                ");
print("");
print("");
print("我TM反了太™棒了");
 
print("================================");
print(" 1. - Nginx启动 -");
print(" 2. - Nginx关闭 -");
print(" 3. - 重启Nginx-");
print(" 4 - Nginx检查配置是否正确 -");
print(" 5 - Nginx安装如果已经安装请不要在安装 -");
print("================================");
command = input("等待输入:  ");
if command == 1: 
    print(" - Nginx启动中... -")
    os.system("//usr//local//webserver//nginx//sbin//nginx")
else:
    if command == 2:
        print("  - Nginx关闭中... -")
        os.system("//usr//local//webserver//nginx//sbin//nginx -s stop")
        print("  - Nginx关闭完成 -")
    else:
        if command == 3:
            print("  - Nginx重启中... -")
            os.system("//usr//local//webserver//nginx//sbin//nginx -s reopen")
            print("  - Nginx重启完成 -")
        else:
            if command == 4:
                print(" - 正在检查Nginx是否正确 - ")
                os.system("//usr//local//webserver//nginx//sbin//nginx -t")
                print("  - 检查完毕 -")
            else:
                 if command == 5:
                    os.system("sh test.sh")
                 else:
                      print(" - 输入错误 - ")
        
    