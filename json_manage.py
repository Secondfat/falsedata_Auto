#coding=utf8
import draw_tiltle
import global_list


# 分离json数据
# 输出存储store_dic  data_temp[key, value, level, fatherlevel, fatherkey, haschild, type]

# 输入data_temp[key, value, level, fatherlevel, fatherkey, states]
def show_dic(data_temp):
    fatherkey = data_temp[0] #提前复制，防止地址擦写
    data_temp[2] = data_temp[2] + 1
    value_temp = data_temp[1]
    if type(value_temp) == dict :
        if (len(data_temp) == 7 or len(data_temp) == 8):
            data_temp[5] = 1
            data_temp[6] = type(value_temp)
        else:
            data_temp.append(1)
            data_temp.append(type(value_temp))
        draw_tiltle.store_dic(data_temp)
        level = data_temp[2]#外部固定fatherlevel
        for key1 ,value1 in value_temp.items():
            data_temp[0] = key1
            data_temp[1] = value1
            data_temp[2] = level#内部固定level
            data_temp[4] = fatherkey
            show_dic(data_temp)
    elif type(value_temp) == list and value_temp != []:
        if (len(data_temp) == 7 or len(data_temp) == 8):
            data_temp[5] = 1
            data_temp[6] = type(value_temp)
        else:
            data_temp.append(1)
            data_temp.append(type(value_temp))
        draw_tiltle.store_dic(data_temp)
        list_num = 0
        for value_list_temp in value_temp:
            list_num += 1
            if (type(value_list_temp)) == dict:
                level = data_temp[2]
                for key_list ,value_list in value_list_temp.items():
                    data_temp[0] = key_list
                    data_temp[1] = value_list
                    data_temp[4] = fatherkey
                    if list_num >= 2:#同一List的不同元素，数据是相同level，因此需要减1
                        data_temp[2] = level - 1
                    else:
                        data_temp[2] = level
                    if len(data_temp) == 7:
                        data_temp.append(list_num)
                    else:
                        data_temp[7] = list_num
                    show_dic(data_temp)
    elif value_temp == []:
        #print("###" + str(len(data_temp)))
        if (len(data_temp) == 7):
            data_temp[5] = 0
            data_temp[6] = type(value_temp)
        else:
            data_temp.append(0)
            data_temp.append(type(value_temp))
        draw_tiltle.store_dic(data_temp)
    else:
        #print("@@@" + str(len(data_temp)))
        if (len(data_temp) == 7 or len(data_temp) == 8):
            data_temp[5] = 0
            data_temp[6] = type(value_temp)
        else:
            data_temp.append(0)
            data_temp.append(type(value_temp))
        draw_tiltle.store_dic(data_temp)
        # else:
        #     data_temp.append(list_num)
        #     draw_tiltle.store_dic(data_temp)


# 生成list下包含所有子节点的数据
def make_new_children(add_pathname):
    #find_children(add_pathname)
    level = global_list.dic_data[add_pathname][0][0]
    flag = 0
    end_flag = 1
    #child_add = []
    for key, value in global_list.dic_data.items():
        if add_pathname in value[4]:
            if flag == 0 and global_list.child_add == [] or flag == 2:
                flag = 1
            else:
                global_list.child_add[len(global_list.child_add) - 1] += ",\n"
            if 'dict' in value[5]:
                father_num = locate_num(key, value, add_pathname)
                global_list.child_add.append("\t" * value[0][father_num] + "\"" + key + "\": {")
                make_new_children(key)
                flag = 2 #防止多一行
            else:
                father_num = locate_num(key, value, add_pathname)
                if value[5][father_num] == "str":
                    global_list.child_add.append("\t" * value[0][father_num] + "\"" + key + "\": " + "\"" + str(value[2][father_num]) + "\"")
                elif value[5][father_num] == "int":
                    global_list.child_add.append("\t" * value[0][father_num] + "\"" + key + "\": " + str(value[2][father_num]))
    global_list.child_add.append("\n" + "\t" * level + "},\n")
    return level

#def list_all_child(all_change_name):



#找到第一个子节点
def locate_num(locate_key, locate_value, add_pathname):
    for i in range(0, len(locate_value[4])):
        if add_pathname == locate_value[4][i]:
            father_num = i
            break
    return father_num



#寻找父节点的函数
def find_father(name, dict):
    if dict[name][4][0] != "top_main":
        temp_name = dict[name][4][0]
        mm = global_list.global_father
        mm.insert(0, temp_name)
        find_father(temp_name, dict)
    else:
        for i in global_list.global_father:
            global_list.link_temp = global_list.link_temp + i + '/'
        #return link_temp
