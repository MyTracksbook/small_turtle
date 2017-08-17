
import sys
sys.setrecursionlimit(1000000)
import os
#filedir = input('请输入目录：')
def file_ext(path):
    allfiles = os.listdir(path='.')
    file_sizes = dict()
    for f in allfiles:
        if os.path.isdir(f):
            file_ext(f)
            os.chdir(os.pardir)
        else:
            file_sizes.setdefault(f,0)
            file_sizes[f] = os.path.getsize(f)
            
    return file_sizes
file_path = input('请输入目录：')
wenjian = file_ext(file_path)
for i in wenjian.keys:
    print('文件%s\t【%s】' % (i,wenjian[i]))
