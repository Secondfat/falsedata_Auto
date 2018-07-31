#coding=utf8
import file_action
import os
import global_list

#生成文件主函数
def do_file(file_path, change_title, change_value):
	if (os.path.exists(file_path)):
		print("do file start......")
		data_temp = global_list.dic_data
		file_name = file_path.split('/')[len(file_path.split('/')) - 1]
		path = file_path.rstrip(file_name).rstrip('/')
		path_temp = os.path.join(path, 'FD_temp')
		if not os.path.exists(path_temp):
			os.makedirs(path_temp)
		change_title_real = []
		for temp in change_title:
			if '/' in temp:
				change_title_real.append(temp.split('/')[len(temp.split('/')) - 1])
				print (change_title_real)
			else:
				change_title_real.append(temp)
				print(change_title_real)
		change_value_real = change_value.split('\n')
		for title in change_title_real:
			for value in change_value_real:
				#print (title + "_!!!!_" + value)
				file_action.change_value(title, global_list.dic_data, file_path, path, value)
		print("do file end......")
	else:
		print("Make file Error!")
