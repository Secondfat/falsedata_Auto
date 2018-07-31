#coding:utf-8
import multiprocessing
from time import sleep
import server_test1
import action_on_phone


#if __name__ == "__main__":
def show_on_phone(file_path, url_change, action_str):
	#print("show_on_phone")
	manager = multiprocessing.Manager()
	stop_flag = manager.list()
	print (len(stop_flag))

	# Define a list (queue) for tasks and computation results
	tasks = manager.Queue()
	results = manager.Queue()

	# Creat process pool with four porcesses
	num_processes = 2
	pool = multiprocessing.Pool(processes = num_processes)
	processes = []

	# Initiate the worker processes
	#for i in range(num_processes):
	# Set process name
		#process_name = 'P%i' % i
	process_name = "P0"
	process_name1 = "P1"

	# Create the process, and connect it to the worker function
	new_process = multiprocessing.Process(target = action_on_phone.action_on_phone, args = (process_name, tasks, results, stop_flag, action_str, file_path))
	new_process1 = multiprocessing.Process(target = server_test1.web_part, args = (process_name1, tasks, results, stop_flag, file_path, url_change))
	#new_process2 = multiprocessing.Process(target= check_app.check_app ,args=())

	# Add new process to the list of processes
	processes.append(new_process)
	print (processes)
	processes.append(new_process1)
	print (processes)

	# Start the process
	new_process.start()
	print("new_peocess")
	new_process1.start()
	print("new_peocess1")


	# Fill task queue
	#task_list = [43, 1, 780, 256, 142, 68, 183, 334, 325, 3]
	#for single_task in task_list:
		#tasks.put(single_task)

	# Wait while the workers process
	sleep(3)

	# Quit the worker processes by sending them -1
	for i in range(num_processes):
		tasks.put(-1)

	# Read calculation results
	num_finished_processes = 0
	while True:
		# Read result
		new_result = results.get()

		# Have a look at the results
		if new_result == -1:
			# Process has finished
			num_finished_processes += 1

			if num_finished_processes == num_processes:
				break
		else:
			# Output result
			print ('Result:' + str(new_result))
