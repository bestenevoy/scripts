import os
import sys
import getpass

# 控制台隐式获取密码

# 使用彩色字体

print('This is a \033[1;35m test \033[0m!')
print('This is a \033[5;32;43m test \033[0m!')
print('\033[1;33;44mThis is a test !\033[0m')

PID = os.getpid()

print('PID', PID)

# 获取当前用户名
USERNAME = getpass.getuser()

# 获取 python 版本信息
PY_VERSION = sys.version_info

# 从控制台获取密码
PASSWORD1 = getpass.getpass(prompt="Password: ")
PASSWORD2 = getpass.getpass(prompt="again: ")

print(PASSWORD1)
print(PASSWORD2)
print(USERNAME)
print(PY_VERSION)
