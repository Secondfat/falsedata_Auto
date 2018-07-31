#coding:utf-8
 
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from random import randint
import show_json
import do_file
import global_list
import control_web


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Gfox_test')
        self.setWindowIcon(QIcon('xdbcb8.ico'))
        self.resize(700, 500)
        self.initUI()
        self.show()

    def initUI(self):

        #定义变量
        self.title_name = []
        #self.change_value = []

        #定义控件
        self.json_file_path = QLineEdit('D:/06 工作/订阅/5.8/test/namedingyue1.json', self)
        self.json_file_path.selectAll()
        self.json_file_path.setFocus()
        self.bt = QPushButton('选择文件')
        self.bt.clicked.connect(self.choose_file_dic)
        self.bt1 = QPushButton('解析文件')
        self.bt1.setToolTip('<b>点击这里猜数字</b>')
        #执行使用的文件
        self.bt1.clicked.connect(lambda:show_json.show_json(self.json_file_path.text()))
        self.bt1.clicked.connect(self.show_port)

        self.value_editor = QPushButton("打开文件", self)
        self.value_editor.clicked.connect(self.openfile)
        self.file_make = QPushButton("生成文件", self)
        self.file_make.clicked.connect(self.mul_file)
        self.file_make.clicked.connect(lambda:do_file.do_file(self.json_file_path.text(), self.title_name, self.show_editor.toPlainText()))
        self.show_editor = QTextEdit()
         
        #self.bt2.setGeometry(620, 50, 200, 30)

        #将光标至于框内
        #self.url_change.setFocus()
        #self.json_file_path.setGeometry(80, 50, 150 ,30)
        #self.url_change.setGeometry(450, 50, 150, 30)

        
        self.main_layout = QVBoxLayout(self)
        up = QHBoxLayout()
        self.middle = QHBoxLayout()
        self.middle_left = QVBoxLayout()
        self.middle_right = QVBoxLayout()
        last = QVBoxLayout()
        self.last_last = QHBoxLayout()

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setGeometry(0, 0, 400, 400)
        self.scroll_area.setAutoFillBackground(True)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_bar = self.scroll_area.verticalScrollBar()

        self.scroll_contents = QWidget()  
        self.scroll_contents.setGeometry(100, 1000, 10, 20)  
        self.scroll_contents.setMinimumSize(1, 1000)
        self.title_confirm = QPushButton("确认选择以下字段", self)
        self.title_confirm.clicked.connect(self.store_title)
        self.middle_left.addWidget(self.title_confirm)
        self.middle_left.addWidget(self.scroll_area)

        self.up_right = QHBoxLayout()
        #self.up_right.addWidget(self.value_change, 0)
        self.up_right.addWidget(self.value_editor, 0)
        self.up_right.addWidget(self.file_make, 0)
        self.middle_right.addWidget(self.show_editor, 0)
        self.middle_right.addLayout(self.up_right)

        self.action_seq = QLineEdit('click,113,1940|down', self)
        self.action_seq.setToolTip('样式如下')
        self.url_change = QLineEdit('http://dev.appsearch.m.sogou.com/user/feed/channel?aa', self)
        #self.url_change.setFocus()
        self.bt2 = QPushButton('开始测试', self)
        self.bt2.clicked.connect(lambda:control_web.control_web(self.json_file_path.text(), self.url_change.text(), self.action_seq.text()))
        last.addWidget(self.action_seq)
        self.last_last.addWidget(self.url_change)
        self.last_last.addWidget(self.bt2)
        
        up.addWidget(self.json_file_path)
        up.addWidget(self.bt)
        up.addWidget(self.bt1)
        #self.middle_left.addWidget(self.result_lb0)
        #last.addWidget(self.url_change)
        #last.addWidget(self.bt2)

        self.main_layout.addLayout(up)
        self.middle.addLayout(self.middle_left)
        self.middle.addLayout(self.middle_right)
        self.main_layout.addLayout(self.middle)
        last.addLayout(self.last_last)
        self.main_layout.addLayout(last)

        self.show()
        
    def choose_file_dic(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "选取文件",
                                                         "D:/",
                                                         "Text Files (*.json)");
        if filename != '':
            self.json_file_path.setText(filename)
        
    #展示每一个接口
    def show_port(self):
        source = self.sender()

        self.scroll_contents = QWidget()  
        self.scroll_contents.setGeometry(100, 1000, 10, 20)  
        self.scroll_contents.setMinimumSize(1, 10000)
        self.middle_left.addWidget(self.scroll_area)

        self.cb = {}
        self.changecb = {}

        #print(global_list.port_name)
        for i, name in enumerate(global_list.port_name):
            self.cb[i] = QCheckBox(name, self.scroll_contents)
            self.cb[i].move(10, 10+i*30)
            #self.scroll_contents.addWidget(self.cb[i])
            #print("##" + self.cb[i].text())
        global_list.port_name = []
        self.scroll_area.setWidget(self.scroll_contents)

    def store_title(self):
        if len(self.title_name) > 0:
            self.title_name = []
        for i in range(0, len(self.cb)):
            if self.cb[i].isChecked():
                self.title_name.append(self.cb[i].text())

    def mul_file(self):
        source = self.sender()
        #self.file_make.clicked.connect(lambda:do_file.do_file(self.json_file_path.text()))
        if len(self.title_name) > 0:
            self.title_name = []
        for i in range(0, len(self.cb)):
            if self.cb[i].isChecked():
                self.title_name.append(self.cb[i].text())
        
    def openfile(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "选取文件",
                                                         "D:/",
                                                         "Text Files (*.txt)");
        print (filename, filetype)
        if filename != '':
            self.r_text=open(filename,'r').read()
            self.show_editor.setPlainText(self.r_text)

    def neme_check(self):
        checkbox = self.sender()
        if state == QT.Checked:
            print("right")
    

    def closeEvent(self, event):
        #我们显示一个带有两个按钮的消息框：Yes和No。
        #第一个字符串出现在标题栏上。
        #第二个字符串是对话框显示的消息文本。
        #第三个参数指定出现在对话框中的按钮的组合。
        #最后一个参数是默认按钮。
        #它是初始键盘焦点的按钮。 返回值存储在答复变量中
        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()        
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
