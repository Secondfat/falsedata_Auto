#coding:utf-8
import re
from socket import *


def url_judge(message, original_url):
	try:
		message = message.decode('utf-8')
	except:
		message = message.decode('unicode_escape')
	print (message)
	requestType = message[0:message.find(" ")].rstrip()
	requestURL = message[0:message.find("HTTP")].split()[1].strip().strip("/")
	r_URL = requestURL[0:len(original_url)]
	if requestType == "GET":
		flag = re.match(original_url, r_URL)
		if flag is not None:
			print ("Already find URL")
			return 1
		else:
			return 0
	elif requestType == "POST":
		return 0
	else:
		return 0

def WebServer_start(file_name, original_url, results, stop_flag):
	# 创建socket，绑定到端口，开始监听
	tcpSerPort = 8899
	tcpSerSock = socket(AF_INET, SOCK_STREAM)

	# Prepare a server socket
	tcpSerSock.bind(('', tcpSerPort))
	tcpSerSock.listen(15)

	while True:
		# 开始从客户端接收请求
		print ('Ready to serve...')
		tcpCliSock, addr = tcpSerSock.accept()
		print ('Received a connection from: ', addr)
		message = tcpCliSock.recv(4096)

		if len(message) != 0:
			flag = url_judge(message, original_url)
			print (flag)

			try:
				if (flag):
					f = open(file_name, 'r', encoding = 'UTF-8')
					outputdata = f.readlines()
					fileExist = "true"
					print ('File Exists!')

					# 缓存中存在该文件，把它向客户端发送
					state_receive = "HTTP/1.0 200 OK\r\n\r\n"
					tcpCliSock.send(bytes(state_receive.encode('utf-8')))
					for i in range(0, len(outputdata)):
						tcpCliSock.send(bytes(outputdata[i].encode('utf-8')))
					print ('Read from cache')
					stop_flag.append(1)
					print ('!!!!!!!!')
					results.put(-1)
					#time.sleep(5)
					break
				else:
					continue
				# 缓存中不存在该文件，异常处理
			except IOError:
				print ('File Exist: ', fileExist)
				if fileExist == "false":
					# 在代理服务器上创建一个tcp socket
					print ('Creating socket on proxyserver')
					c = socket(AF_INET, SOCK_STREAM)

					hostn = filename.replace("www.", "", 1)
					print ('Host Name: ', hostn)
					try:
						# 连接到远程服务器80端口
						c.connect((hostn, 80))
						print ('Socket connected to port 80 of the host')

						# 在代理服务器上缓存请求的文件
						fileobj = c.makefile('r', 0)
						#拼凑http get请求的请求行。注意格式为： "请求方法 URI HTTP版本"，空格不能省略!
						fileobj.write("GET " + "http://" + filename + " HTTP/1.0\n\n")

						# Read the response into buffer
						buff = fileobj.readlines()

						# Create a new file in the cache for the requested file.
						# Also send the response in the buffer to client socket
						# and the corresponding file in the cache
						tmpFile = open("./" + filename, "wb")
						for i in range(0, len(buff)):
							tmpFile.write(buff[i])
							tcpCliSock.send(buff[i])

					except:
						print ("Illegal request")

				else:
					# HTTP response message for file not found
					# Do stuff here
					print ('File Not Found...Stupid Andy')
					a = 2
			# Close the client and the server sockets
			tcpCliSock.close()
		else:
			continue
	# Fill in start.
	tcpSerSock.close()

#if __name__ == '__main__':
def web_part(process_name, tasks, results, stop_flag, file_path, url_change):
	print('[%s] evaluation routine starts' % process_name)
	print("###")
	#file_name = "liudehuadianying.json"
	#original_url = "http://dev.appsearch.m.sogou.com/sugg"
	#				http://dev.appsearch.m.sogou.com/sugg?
	#stop_flag = []
	#results = 1
	WebServer_start(file_path, url_change, results, stop_flag)

	#return results
	print("test")