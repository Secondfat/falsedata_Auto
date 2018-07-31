#coding:utf-8
 
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon
from random import randint
import show_json


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Gfox_test')
        self.setWindowIcon(QIcon('xdbcb8.ico'))
        self.resize(700, 500)
        self.initUI()
        self.show()

    def initUI(self):
        main_layout = QVBoxLayout(self)

        
        
        self.setGeometry(300, 300, 800, 620)

        self.bt1 = QPushButton('解析文件', self)
        self.bt1.setGeometry(250, 50, 80, 30)
        #self.bt1.setToolTip('<b>点击这里猜数字</b>')

        self.bt2 = QPushButton('确定', self)
        self.bt2.setGeometry(620, 50, 50, 30)
        #self.bt2.setToolTip('<b>点击这里猜数字</b>')

        #按钮被点击时调用showMessage的方法去响应   
        self.bt1.clicked.connect(lambda :show_json.show_json(self.json_file_path.text()))
        #self.bt1.clicked.connect(self.showMessage)

        #初始默认字符
        self.url_change = QLineEdit('在这里输入匹配URL', self)
        self.json_file_path = QLineEdit('在这里输如文件路径', self)
        #将框里字符全选
        self.json_file_path.selectAll()
        self.url_change.selectAll()
        #将光标至于框内
        #self.url_change.setFocus()
        self.json_file_path.setGeometry(80, 50, 150 ,30)
        self.url_change.setGeometry(450, 50, 150, 30)
        
    def showMessage(self):
        #将输入的str格式转为int
        guessnumber = self.json_file_path.text()
        print(guessnumber)`
        QMessageBox.about(self,'',guessnumber)

##        if guessnumber > self.num:
##            QMessageBox.about(self, '看结果','猜大了!')
##            self.text.setFocus()        
##        elif guessnumber < self.num:
##            QMessageBox.about(self, '看结果','猜小了!')
##            self.text.setFocus()       
##        else:
##            QMessageBox.about(self, '看结果','答对了!进入下一轮!')
##            self.num = randint(1,100)
##            self.text.clear()
##            self.text.setFocus()

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
