#coding:utf-8
import json
import json_manage
import global_list


#替换字段数据并存储
def change_value(key_change, data_dic_temp, filepath, path, value_change):
    with open (filepath, encoding='utf-8') as load_f:
        lines = load_f.readlines()
        for i in range(0, len(lines)):
            if ":" in lines[i]:
                key = lines[i].split(":")[0].split("\"")[1]
                print (key)
                if key == key_change:
                    lines[i] = lines[i].replace(str(data_dic_temp[key][2]), str(value_change))
                    break
    new_filepath = path + "//FD_temp//" + key_change + "_" + value_change + ".json"
    with open (new_filepath,'w') as new_f:
        new_f.writelines(lines)
    load_f.close()

# #增加列表中的一个数据
# def add_list():
#     with


#存储产生的json字段
def file_storage(data_temp, path):
    file_name = path + '/temp_data.json'
    f = open(file_name, "w")
    json.dump(data_temp, f)
    f.close()


# 文件list下添加字段
def add_list(file_path, add_pathname):
    #global_list.child_add = []
    with open (file_path, encoding='utf-8') as load_f:
        lines = load_f.readlines()
        lines_out = []
        flag = 0
        for i in range(0, len(lines)):
            if flag == 0:
                lines_out.append(lines[i])
            if flag == 0 and add_pathname in lines[i]:
                flag += 1
            if flag == 1 and "[" in lines[i]:
                flag += 1
            if flag == 2 and "{" in lines[i]:
                flag += 1
            if flag == 3:
                if (len(lines[i].split("{")) > 1):
                    if (":" in lines[i].split("{")[1]):
                        tab_num = json_manage.make_new_children(add_pathname)
                        for each_add in global_list.child_add:
                            lines_out.append(each_add)
                        lines_out.append("\t" * tab_num + "{\n")
                        flag = 4
                elif ("{" not in lines[i] and ":" in lines[i]):
                    tab_num = json_manage.make_new_children(add_pathname)
                    for each_add in global_list.child_add:
                        lines_out.append(each_add)
                    lines_out.append("\t" * tab_num + "{\n")
                    flag = 4
            if flag == 4:
                lines_out.append(lines[i])
    global_list.child_add = []
    new_filepath = "ttt.json"
    with open(new_filepath, 'w') as new_f:
        new_f.writelines(lines_out)
    load_f.close()


def list_all_key(file_path, add_pathname):
    # with open (file_path, encoding='utf-8') as load_f:
    #     lines = load_f.readlines()
    print("1")



#实验版替换
# def change_value_temp(key_change, data_dic_temp, path, value_change):
#     json_manage.find_father(key_change,data_dic_temp)
#     global_list.global_father.append(key_change)
#     fathers = global_list.global_father
#     fathers_len = len(fathers)
#     with open (path, encoding='utf-8') as load_f:
#         load_dict = json.load(load_f)
#         load_dict_temp = load_dict
#         print(load_dict_temp)
#         mm = "[" + fathers[0] + "]"
#         for temp in range(0, fathers_len):
#             name_list= fathers[temp]
#             if data_dic_temp[name_list][5] == 'dict':
#                 mm = mm + "[" + name_list + "]"
#                 load_dict_temp = load_dict_temp[name_list]
#             elif data_dic_temp[name_list][5] == 'list':
#                 load_dict_temp = load_dict_temp[name_list][0]
#                 mm = mm + "[" + name_list + "]" + "[0]"
#                 #mm = mm[name_list][0]
#                 #print (load_dict_temp)
#             else:
#                 mm = mm + "[" + key_change + "]"
#                 load_dict_temp = load_dict_temp[key_change]
#         old_value = "\"" + name_list + "\"" + ": " + "\"" + load_dict_temp + "\""
#         new_value = "\"" + name_list + "\"" + ": " + "\"" + value_change + "\""
#         #load_f.replace(old_value, new_value)
#         data = load_f.read()
#         print (data)
#     load_f.close()

