#coding:utf-8
 
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from random import randint
import show_json
import global_list

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Gfox_test')
        self.setWindowIcon(QIcon('xdbcb8.ico'))
        self.resize(700, 500)
        self.initUI()
        self.show()

    def initUI(self):

        #定义控件
        self.json_file_path = QLineEdit('D:/06 工作/订阅/5.8/type假数据/test_bianli.json', self)
        self.json_file_path.selectAll()
        self.json_file_path.setFocus()
        self.bt = QPushButton('选择文件')
        self.bt.clicked.connect(self.choose_file_dic)
        self.bt1 = QPushButton('解析文件')
        #self.bt1.setGeometry(250, 50, 80, 30)
        self.bt1.setToolTip('<b>点击这里猜数字</b>')
        self.bt1.clicked.connect(lambda:show_json.show_json(self.json_file_path.text()))
        self.bt1.clicked.connect(self.show_port)
        #print (mm)
        #mm.result1_window.setText()
        self.result_lb0 = QLabel('可修改数据',self)
        #self.result_lb0.setGeometry(50, 100, 50, 30)
        #result_temp = QLabel(mm, self)
        #lb6.setText(text)
        self.url_change = QLineEdit('在这里输入匹配URL', self)
        #self.url_change.setFocus()
        self.bt2 = QPushButton('确定', self)
        self.bt2.setGeometry(620, 50, 50, 30)

        #将光标至于框内
        #self.url_change.setFocus()
        self.json_file_path.setGeometry(80, 50, 150 ,30)
        self.url_change.setGeometry(450, 50, 150, 30)

        self.main_layout = QVBoxLayout(self)
        up = QHBoxLayout()
        self.middle = QHBoxLayout()
        self.middle_left = QVBoxLayout()
        self.middle_right = QVBoxLayout()
        last = QHBoxLayout()

##        scroll = QScrollArea() 
##        scroll.setWidget(self.middle)  
##        scroll.setAutoFillBackground(True)  
##        scroll.setWidgetResizable(True)
##        self.middle.addWidget(scroll)
        
        up.addWidget(self.json_file_path)
        up.addWidget(self.bt)
        up.addWidget(self.bt1)
        self.middle_left.addWidget(self.result_lb0)
        last.addWidget(self.url_change)
        last.addWidget(self.bt2)

        self.main_layout.addLayout(up)
        self.middle.addLayout(self.middle_left)
        self.middle.addLayout(self.middle_right)
        self.main_layout.addLayout(self.middle)
        self.main_layout.addLayout(last)


        self.show()
        
    def choose_file_dic(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "选取文件",
                                                         "D:/",
                                                         "Text Files (*.json)");
        if filename != '':
            self.json_file_path.setText(filename)
        

    def show_port(self):
        source = self.sender()
        #self.bt1.clicked.connect(lambda:show_json.show_json(self.json_file_path.text()))
        self.cb = {}
        self.changecb = {}
        for i, name in enumerate(global_list.port_name):
            self.cb[i] = QCheckBox(name, self)
            self.cb[i].move(20, 20)
            #self.cb[i].stateChanged.connect(self.name_check)
            #self.cb[i].toggle()
            self.middle_left.addWidget(self.cb[i])
            #print (self.cb[i])
        self.value_change = QLineEdit(self.json_file_path.text(), self)
        self.value_editor = QPushButton("打开文件", self)
        self.value_editor.clicked.connect(self.openfile)
        self.show_editor = QTextEdit()

        self.up_right = QHBoxLayout()
        self.up_right.addWidget(self.value_change, 0)
        self.up_right.addWidget(self.value_editor, 0)
        self.middle_right.addWidget(self.show_editor, 0)
        
        self.middle_right.addLayout(self.up_right)
        
        #clear_bt = 
        #self.bt1.clicked.connect()
        #global_list.port_name = []
        #self.show()

    #def show_value(self):
        
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
        if state== QT.Checked:
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
