# 导入所需模块
import subprocess
import sys
import time

# 工具函数模块

# 工具函数：清屏函数
def clear_screen():
    # Windows 系统
    if sys.platform.startswith("win"):
        subprocess.run("cls", shell=True, check=True)
    # macOS / Linux 系统
    else:
        subprocess.run("clear", shell=True, check=True)

# 工具函数：延时函数
# i (int/float): 延时的秒数，可以是整数或浮点数
def delay(i):

    time.sleep(i)

# 检查用户
def check_user():
    


# 主程序
clear_screen()

print("欢迎来到练习考试系统！")
