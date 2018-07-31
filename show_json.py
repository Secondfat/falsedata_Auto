#coding:utf-8

import draw_tiltle
import json
import json_manage
import global_list
import file_action
import os

#dic_data={}

#解析json文件主函数
if __name__ == '__main__':
#def show_json(file_path):
    #file_path = 'E:/07 学习/Python-tools/7.12/namedingyue.json'
    file_path = 'D:/06 工作/订阅/5.8/type假数据/namedingyue.json'
    if(os.path.exists(file_path)):
        print(file_path)
        global_list.dic_data = {}
        file_name = file_path.split('/')[len(file_path.split('/'))-1]
        path = file_path.rstrip(file_name).rstrip('/')
        fp = open(file_path, encoding='utf-8')
        data = fp.read()
        hjson = json.loads(data)
        data_temp = draw_tiltle.draw_txt(file_path)
        print(data_temp)
        file_action.file_storage(data_temp, path)
        for key, value in data_temp.items():
            if value[1] == 0:
                json_manage.find_father(key, data_temp)
                #print(key, global_list.link_temp + key)
                global_list.port_name.append(global_list.link_temp + key)
                global_list.global_father = []
                global_list.link_temp = ''
            else:
                continue
        #return 1
    else:
        print("no file!")

    # # 在list下复制第一个元素
    # add_pathlist = "result/kwacc_list"
    # add_pathname = add_pathlist.split('/')[-1]
    # file_action.add_list(file_path, add_pathname)

    #将list下所有string变成一个值，int变成一个值
    add_pathlist = "result/kwacc_list"
    add_pathname = add_pathlist.split('/')[-1]
    file_action.list_all_key(file_path, add_pathname)

