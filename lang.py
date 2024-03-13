from pymem import pymem
import os

divs = {'AX':0,'BX':0,'CX':0,'DX':0,'EX':0,}

def clas(code):
    global divs
    for i in range(len(code)):
        cache = code[i]
        ddd = cache
        cache = cache.split(' ',1)
        if cache[0] == 'print':
            if (cache[1] == 'AX\n') or (cache[1] == 'BX\n') or (cache[1] == 'CX\n') or (cache[1] == 'DX\n') or (cache[1] == 'EX\n') or (cache[1] == 'AX') or (cache[1] == 'BX') or (cache[1] == 'CX') or (cache[1] == 'DX') or (cache[1] == 'EX'):
                print(divs[cache[1].replace('\n','')])
            else:
                print(cache[1].replace('\n',''))
        elif (cache[0] == 'AX') or (cache[0] == 'BX') or (cache[0] == 'CX') or (cache[0] == 'DX') or (cache[0] == 'EX'):
            if (cache[1].replace('\n','') != 'AX') or (cache[1].replace('\n','') != 'BX') or (cache[1].replace('\n','') != 'CX') or (cache[1].replace('\n','') != 'DX') or (cache[1].replace('\n','') != 'EX'):
                divs[cache[0].replace('\n','')] = int(cache[1].replace('\n',''))
            else:
                divs[cache[0].replace('\n','')] = divs[cache[1].replace('\n','')]
        if (cache[0] == 'P'):
            if (cache[1] == 'AX') or (cache[1] == 'BX') or (cache[1] == 'CX') or (cache[1] == 'DX') or (cache[1] == 'EX'):
                if (cache[2].replace('\n','') != 'AX') or (cache[2].replace('\n','') != 'BX') or (cache[2].replace('\n','') != 'CX') or (cache[2].replace('\n','') != 'DX') or (cache[2].replace('\n','') != 'EX'):
                    divs[cache[1].replace('\n','')] = divs[cache[1].replace('\n','')] + int(cache[2].replace('\n',''))
                else:
                    divs[cache[1].replace('\n','')] = divs[cache[1].replace('\n','')] + divs[cache[2].replace('\n','')]
        elif (cache[0] == 'input'):
            divs[cache[1].replace('\n','')] = int(input())
        elif (cache[0] == 'if'):
            cache = ddd.split(' ')
            if (divs[cache[1].replace('\n','')] == int(cache[2])):
                o = open(cache[3].replace('\n',''),mode='r')
                t = o.readlines()
                o.close()
                clas(t)
        elif (cache[0] == 'mif'):
            cache = ddd.split(' ')
            if (divs[cache[1].replace('\n','')] > int(cache[2])):
                o = open(cache[3].replace('\n',''),mode='r')
                t = o.readlines()
                o.close()
                clas(t)
        elif (cache[0] == 'lif'):
            cache = ddd.split(' ')
            if (divs[cache[1].replace('\n','')] < int(cache[2])):
                o = open(cache[3].replace('\n',''),mode='r')
                t = o.readlines()
                o.close()
                clas(t)
        elif (cache[0] == 'mem'):
            cache = ddd.split(' ')
            pm = pymem(cache[1])
            if cache[2] == 'read':
                print(pm.read_int(int(cache[2].replace('\n',''))))
            else:
                pm.write_int(int((cache[3].replace('\n','')),base=16),(cache[4].replace('\n','')))
        elif (cache[0] == 'sys'):
            os.system(cache[1].replace('\n',''))
        else:
            print('行',i+1,':语法错误')
def main():
    codes = input("DY Comp ->")
    let = open(codes,mode='r')
    t = let.readlines()
    let.close()
    clas(t)

while 1:
    main()

#示例程序
#print AX
#AX 5
#print AX
#input AX
#print AX
#if AX 5 test.dy
#mem sb.exe write 0x22222 2222
    
#文档
#print 参数
#打印,字符串不用加'',如果是虚拟寄存器,打印虚拟寄存器的值
#寄存器1 寄存器2/数字
#将前一个寄存器名赋值为后面的数/寄存器的值
#P 寄存器1 寄存器2/数字
#将寄存器/数字相加，把和保存至寄存器1
#input 寄存器
#将输入的值保存至寄存器
#if 寄存器 数字 文件名
#mif 寄存器 数字 文件名
#lif 寄存器 数字 文件名
#等于/大于/小于时，执行文件
#mem 程序名 write/read 地址 值(only write)
#写入/读取程序的内存
#sys 命令
#执行命令
