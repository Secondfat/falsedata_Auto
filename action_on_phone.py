#coding:utf8
from action import *
import global_list


def action_on_phone(process_name, tasks, results, stop_flag, action_str, file_path):
	print('[%s] evaluation routine starts' % process_name)
	print("#")
	#element = element.Element()
	device_id = Get_DeviceId()[0]
	Start_Activity(device_id,"com.sogou.activity.src/com.sogou.search.entry.EntryActivity")
	time.sleep(5)
	#try:
	for action_do in action_str:
		if action_do == 'up':
			Swipe_Up(device_id)
			time.sleep(2)
		elif action_do == 'down':
			Swipe_Down(device_id)
			time.sleep(2)
		elif 'click' in action_do:
			label_click = action_do.split(',')
			Click(device_id, x = label_click[1], y = label_click[2])
		elif 'input' in action_do:
			if 'always' in action_do:
				while len(stop_flag) == 0:
					data_temp = action_do.split(' ')
					Input_Text(device_id, data_temp)
					time.sleep(2)
			else:
				data_temp = action_do.split(' ')
				Input_Text(device_id, data_temp)
				time.sleep(2)
		time.sleep(3)
	file_name = file_path.split('/')[len(file_path.split('/')) - 1].rstrip('.json')
	path = file_path.rstrip(file_name).rstrip('/')
	path_image = path + '\image'
	if not os.path.exists(path_image):
		os.makedirs(path_image)
	image_app_name = "image_" + file_name + ".png"
	Get_Screencap(device_id, image_app_name, path_image)
	crash_out = check_app(device_id)
	if crash_out == False:
		global_list.iscrash = 1
	results.put(-1)
