#coding=utf8

import json
import json_manage
import global_list



#初始化词典
#dic_data={}
cnt = 0


def cnt_global():
    global cnt
    cnt = cnt + 1


#按照格式存储数据到字典中
# data_temp[key, value, level, fatherlevel, fatherkey, haschild, type]
def store_dic(data_temp):
    key = data_temp[0]
    value = data_temp[1]
    level = data_temp[2]
    fatherlevel = data_temp[3]
    fatherkey = data_temp[4]
    haschild = data_temp[5]
    type_data = data_temp[6]
    #listnum = data_temp[7]
    if type_data == str:
        type_data = "str"
    elif type_data == dict:
        type_data = "dict"
    elif type_data == int:
        type_data = "int"
    elif type_data == list:
        type_data = "list"


    if (global_list.dic_data.__contains__(data_temp[0]) == False):
        if (data_temp[5] == 1):
            global_list.dic_data[data_temp[0]] = [[data_temp[2]], data_temp[5], [""], [data_temp[3]], [data_temp[4]], [type_data]]
        else:
            if(len(data_temp) == 8):
                global_list.dic_data[data_temp[0]] = [[data_temp[2]], data_temp[5], [data_temp[1]], [data_temp[3]], [data_temp[4]], [type_data], [data_temp[7]]]
            else:
                global_list.dic_data[data_temp[0]] = [[data_temp[2]], data_temp[5], [data_temp[1]], [data_temp[3]], [data_temp[4]], [type_data]]
    else:
        #print (data_temp[5])
        if (data_temp[5] == 1):
            return True
        else:
            global_list.dic_data[data_temp[0]][0].append(data_temp[2])
            global_list.dic_data[data_temp[0]][2].append(data_temp[1])
            global_list.dic_data[data_temp[0]][4].append(data_temp[4])
            global_list.dic_data[data_temp[0]][5].append(type_data)
            #print(data_temp)
            if (len(data_temp) == 8):
                global_list.dic_data[data_temp[0]][6].append(data_temp[7])
            return True
            #dic_data[key][2] = value

#读取文件
def draw_txt(path):
    fp = open(path,encoding='utf-8')
    data = fp.read()
    hjson = json.loads(data)
    #print (hjson)
    for key,value in hjson.items():
        #print ("###" + key)
        temp_data = []
        level = 0
        #print (value)
        temp_data.extend([key, value, level, 1, "top_main"])
        #print(temp_data)
        json_manage.show_dic(temp_data)
    fp.close()
    return global_list.dic_data

#主函数
#if __name__ == '__main__':
#    path = 'D:/06 工作/订阅/5.8/type假数据/test_bianli.json'
#    draw_txt(path)
#    for i,j in dic_data.items():
#        print("key=",i,"value=",j)

