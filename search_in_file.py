import os
def print_pos(key_dict):
    keys = sorted(key_dict.keys())
    for i in keys:
        print('关键字出现在%s行%s个字符'%（i,str(key_dict[i])）)
    

def search_in_line(line,key):
    begin = line.find(key):
        weizhi = []
        while begin != -1:
            weizhi.append(begin + 1)
            begin = line.find(key,begin + 1)
        return weizhi

def search_in_file(filename,key):
    #输出一个字典，记录key所在的具体行数
    f = open(filename)
    count = 0
    key_dict = dict()

    for i in f:
        count += 1
        if key in i:
            pos = search_in_line(i,key)
            key_dict[count] = pos

    f.close()
    return key_dict


def search_file(key,detail):
    all_file = os.walk(os.getcwd)
    txt_file = []
    for root,dir,file in all_file:
        if os.path.splitext(file)[1] == '.txt':
            each_file = os.path.join(root,file)
            txt_file.append(each_file)

    for each_txt_file in txt_file:
        key_dict = search_in_file(filename,key)
        if key_dict:
            print('在%s文件中找到关键字%s' % (each_txt_file,key))
            if detail in ['Y','y','yes','YES']:
                print_pos(key_dict)
                
