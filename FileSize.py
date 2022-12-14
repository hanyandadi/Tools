import os
import sys
import time


def getusername():
    namelist = os.popen('echo %username%').readlines()
    username = namelist[0].replace("\n", "")
    return username


# 获取时间和日期
def getnowdatatime(flag=0):
    '''
    flag = 0为时间和日期         eg:2018-04-11 10:04:55
    flag = 1仅获取日期           eg:2018-04-11
    flag = 2仅获取时间           eg:10:04:55
    flag = 3纯数字的日期和时间    eg:20180411100455
    '''
    now = time.localtime(time.time())
    if flag == 0:
        return time.strftime('%Y-%m-%d %H:%M:%S', now)
    if flag == 1:
        return time.strftime('%Y-%m-%d', now)
    if flag == 2:
        return time.strftime('%H:%M:%S', now)
    if flag == 3:
        return time.strftime('%Y%m%d%H%M%S', now)


# 生成指定大小的TXT档
def generateTXTByteFile():
    size = input('请输入你想生成的TXT文件大小(Byte):')
    fileSize = int(size)

    # 生成指定大小的TXT档
    filename = getnowdatatime(3) + '_' + size + 'Byte.txt'
    print(f'文件名：{filename}')
    # 设置文件保存的路径
    filepath = 'C:\\Users\\' + getusername() + '\\Desktop\\'
    f = open(filepath + filename, 'w')
    # 获取开始时间
    starttime = getnowdatatime()
    startclock = time.perf_counter()
    for i in range(fileSize):
        try:
            f.write('1')
        except KeyboardInterrupt:
            print('\n异常中断:KeyboardInterrupt')
            f.close()
            exit(-1)
    f.close()
    print(f'文件已成生并保存在桌面,  文件大小:{fileSize}Byte.\n')
    print(f'DetailInfo:')
    print(f'保存路径: {filepath + filename}')
    print(f'开始时间:{starttime}')
    print(f'结束时间:{getnowdatatime()}')
    print(f'总共耗时:{(time.perf_counter() - startclock):<.3}sec.')

def generateTXTMBFile():
    fileSize = 0
    while True:
        size = input('请输入你想生成的TXT文件大小(MB):')
        if size.strip().isdigit() != True:
            print('只能输入整数，请重新输入!')
            continue
        else:
            fileSize = int(size)
            break
    if fileSize >= 200:
        print('正在生成TXT文件，请稍候... ...')
    # 生成指定大小的TXT档
    filename = getnowdatatime(3) + '_' + size + 'MB.txt'
    print(f'文件名：{filename}')
    # 设置文件保存的路径
    filepath = 'C:\\Users\\' + getusername() + '\\Desktop\\'
    f = open(filepath + filename, 'w')
    # 获取开始时间
    starttime = getnowdatatime()
    startclock = time.perf_counter()
    for i in range(fileSize):
        if i >= 100:
            if i % 100 == 0:
                print(f'已生成{i//100 * 100}MB数据.')
        for j in range(1024):
            try:
                f.write('01' * 512)
            except KeyboardInterrupt:
                print('\n异常中断:KeyboardInterrupt')
                f.close()
                exit(-1)
    f.close()
    print(f'文件已成生并保存在桌面,  文件大小:{fileSize}MB.\n')
    print(f'DetailInfo:')
    print(f'保存路径: {filepath + filename}')
    print(f'开始时间:{starttime}')
    print(f'结束时间:{getnowdatatime()}')
    print(f'总共耗时:{(time.perf_counter() - startclock):<.3}sec.')

def generateTXTGBFile():
    fileSize = 0
    # 判断输入是否有误
    while True:
        size = input('请输入你想生成的TXT文件大小(GB):')
        if size.strip().isdigit() != True:
            print('只能输入整数，请重新输入!')
            continue
        else:
            fileSize = int(size)
            break
    if fileSize >= 200:
        print('正在生成TXT文件，请稍候... ...')
    # 生成指定大小的TXT档
    filename = getnowdatatime(3) + '_' + size + 'GB.txt'
    print(f'文件名：{filename}')
    # 设置文件保存的路径
    filepath = 'C:\\Users\\' + getusername() + '\\Desktop\\'
    f = open(filepath + filename, 'w')
    # 获取开始时间
    starttime = getnowdatatime()
    startclock = time.perf_counter()
    for i in range(fileSize):
        if i >= 100:
            if i % 100 == 0:
                print(f'已生成{i//100 * 100}GB数据.')
        for j in range(1024):
            try:
                f.write('01' * 524288)
            except KeyboardInterrupt:
                print('\n异常中断:KeyboardInterrupt')
                f.close()
                exit(-1)
    f.close()
    print(f'文件已成生并保存在桌面,  文件大小:{fileSize}GB.\n')
    print(f'DetailInfo:')
    print(f'保存路径: {filepath + filename}')
    print(f'开始时间:{starttime}')
    print(f'结束时间:{getnowdatatime()}')
    print(f'总共耗时:{(time.perf_counter() - startclock):<.3}sec.')

def menucontrol():
    command = int(input('请输入所需文件大小【0:Byte/1:MB/2:GB/3:退出】：'))
    if command == 0:
        generateTXTByteFile()
        menucontrol()
    elif command == 1:
        generateTXTMBFile()
        menucontrol()
    elif command == 2:
        generateTXTGBFile()
        menucontrol()
    elif command == 3:
        sys.exit()
    else:
        print("您输入错误信息，请重新输入！")
        menucontrol()


if __name__ == '__main__':
    print('\033[31mThe Version Of This Software is V0.0.2\033[0m')
    menucontrol()

