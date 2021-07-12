# -*- coding = utf-8 -*-
# @Time : 2021/7/11 22:06
# @Author : 刘正阳
# @File : test.py
# @Software : PyCharm

s = {}
s[0]=1
print(s[0])

from PyQt5.QtWidgets import *
i = 0
class DynamicAdd(QDialog):
    def __init__(self):
        super().__init__()
        #在水平布局上动态添加label
        self.main_layout = QGridLayout()

        self.btn = QPushButton('老八')
        self.main_layout.addWidget(self.btn,0,0,1,88)

        #self.h_layout = QHBoxLayout()
        self.label = {}
        self.label[0] = QLabel('撤硕0号')
        self.main_layout.addWidget(self.label[0], 1, 0)
        # self.main_layout.addLayout(self.h_layout,1,0)
        self.btn.clicked.connect(self.add)
        self.setLayout(self.main_layout)
    def add(self):
        global i
        i += 1
        self.label[i] = QLabel('撤硕%s号'%i)
        #self.h_layout.addWidget(self.label[i])
        self.main_layout.addWidget(self.label[i],1,i)#第一行第i列



if __name__ =='__main__':
    import sys
    app = QApplication(sys.argv)
    gpa = DynamicAdd()
    gpa.show()
    sys.exit(app.exec_())
    a = b'd'