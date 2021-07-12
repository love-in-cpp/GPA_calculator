# -*- coding = utf-8 -*-
# @Time : 2021/7/11 20:39
# @Author : 刘正阳
# @File : main.py
# @Software : PyCharm
import base64
import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from icon import img
index = 0


class GPA_calculator(QDialog):

    def __init__(self, parent=None):
        super(GPA_calculator, self).__init__()
        # 设置自定义样式
        super(GPA_calculator, self).__init__(parent)
        self.v_layout = {}
        self.grade_text = {}
        self.lab_grade = {}
        self.point_text = {}
        self.lab_point = {}
        self.lab_obj = {}
        self.originalPalette = QApplication.palette()
        self.current_row = 1
        self.current_column = 1

        self.center_group = {}
        self.center_group[index] = QGroupBox()
        self.createCenterGroup(index)

        self.btn = QPushButton('添加')
        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.btn)
        self.btn.clicked.connect(self.btn_f)

        self.btn1 = QPushButton('计算')
        self.btn1.clicked.connect(self.get_result)
        self.text = QLineEdit()
        self.lab = QLabel('平均学分：')
        self.lab.setBuddy(self.text)

        self.text1 = QLineEdit()
        self.lab1 = QLabel('平均绩点：')
        self.lab1.setBuddy(self.text1)

        self.text2 = QLineEdit()
        self.lab2 = QLabel('平均学分绩点：')
        self.lab2.setBuddy(self.text2)
        # self.h_layout1 = QHBoxLayout()
        # self.h_layout1.addWidget(self.lab)
        # self.h_layout1.addWidget(self.text)
        self.btn3 = QPushButton('关于')
        self.btn3.clicked.connect(self.show_about_dialog)

        self.main_layout = QGridLayout()
        self.main_layout.addLayout(self.h_layout, 0, 0, 1, 8)
        # self.main_layout.addWidget(self.btn)
        self.main_layout.addWidget(self.center_group[index], 1, 0, 1, 1)
        # self.main_layout.setSizeConstraint()
        self.main_layout.addWidget(self.btn1, self.current_row + 1, 0, 1, 8)
        self.main_layout.addWidget(self.lab, self.current_row + 2, 0)
        self.main_layout.addWidget(self.text, self.current_row + 2, 1, 1, 2)
        self.main_layout.addWidget(self.lab1, self.current_row + 3, 0)
        self.main_layout.addWidget(self.text1, self.current_row + 3, 1, 1, 2)
        self.main_layout.addWidget(self.lab2, self.current_row + 4, 0)
        self.main_layout.addWidget(self.text2, self.current_row + 4, 1, 1, 2)
        self.main_layout.addWidget(self.btn3, self.current_row + 5, 0, 1, 8)
        # self.main_layout.addLayout(self.h_layout1, self.current_row + 2, 0, 1, 2)
        # self.setWindowFlags(Qt.WindowMinMaxButtonsHint)
        self.setWindowFlags(Qt.WindowContextHelpButtonHint | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        # self.setWindowFlags(Qt.WindowContextHelpButtonHint)
        tmp = open('tmp.png',"wb+")
        tmp.write(base64.b64decode(img))
        tmp.close()
        icon = QIcon('tmp.png')
        os.remove("tmp.png")
        self.setWindowIcon(icon)

        self.setLayout(self.main_layout)
        # cw = QWidget()
        # cw.setLayout(self.main_layout)
        # self.setCentralWidget(cw)
        self.setWindowTitle('平均学分绩点计算器')
        self.setFixedWidth(1200)
        # self.setBaseSize(500,500)

    def btn_f(self):
        global index

        index = index + 1

        self.center_group[index] = QGroupBox()
        self.createCenterGroup(index)
        if index % 8 == 7:
            self.main_layout.addWidget(self.center_group[index], self.current_row, self.current_column, 1, 1)
            self.current_row += 1
            self.current_column = 0

        else:
            self.main_layout.addWidget(self.center_group[index], self.current_row, self.current_column, 1, 1)
            # self.current_row += 1
            self.current_column += 1
        self.main_layout.addWidget(self.btn1, self.current_row + 1, 0, 1, 8)
        # self.main_layout.addLayout(self.h_layout1, self.current_row + 2, 0, 1, 2)
        self.main_layout.addWidget(self.lab, self.current_row + 2, 0)
        self.main_layout.addWidget(self.text, self.current_row + 2, 1, 1, 2)

        self.main_layout.addWidget(self.lab1, self.current_row + 3, 0)
        self.main_layout.addWidget(self.text1, self.current_row + 3, 1, 1, 2)

        self.main_layout.addWidget(self.lab2, self.current_row + 4, 0)
        self.main_layout.addWidget(self.text2, self.current_row + 4, 1, 1, 2)
        self.main_layout.addWidget(self.btn3, self.current_row + 5, 0, 1, 8)

    def createCenterGroup(self, i):

        self.lab_obj[i] = QLabel('科目%s：' % (i + 1))

        self.lab_point[i] = QLabel('学分%s：' % (i + 1))
        self.point_text[i] = QLineEdit()
        self.lab_point[i].setBuddy(self.point_text[i])

        self.lab_grade[i] = QLabel('绩点%s：' % (i + 1))
        self.grade_text[i] = QLineEdit()
        self.lab_grade[i].setBuddy(self.grade_text[i])

        self.v_layout[i] = QVBoxLayout()
        self.v_layout[i].addWidget(self.lab_obj[i])
        self.v_layout[i].addWidget(self.lab_point[i])
        self.v_layout[i].addWidget(self.point_text[i])
        self.v_layout[i].addWidget(self.lab_grade[i])
        self.v_layout[i].addWidget(self.grade_text[i])

        self.center_group[i].setLayout(self.v_layout[i])
        # self.get_result()

    # point 是绩点 grade 是学分
    def get_result(self):
        # print(len(self.point_text))
        sum_grade = 0
        avg_grade = 0
        sum_point = 0
        avg_point = 0
        sum_gp = 0
        result = 0
        empty_point = 0
        empty_grade = 0

        for i in range(0, len(self.point_text)):
            # print('6666666666')
            if self.point_text[i].text() == '' or self.point_text[i].text() == '0':
                self.point_text[i].setText('0')
                #empty_point += 1

            if self.grade_text[i].text() == '' or self.grade_text[i].text() == '0':
                self.grade_text[i].setText('0')
                #empty_grade += 1
            sum_grade += float(self.point_text[i].text())
            # print(1)
            sum_point += float(self.grade_text[i].text())
            # print(2)
            sum_gp += (float(self.point_text[i].text()) * float(self.grade_text[i].text()))
            # print(3)
        print(sum_gp)
        print(sum_point)
        print(sum_grade)
        # print(self.point_text[i].text())
        print(empty_grade)
        if len(self.point_text) - int(empty_grade) != 0:
            avg_grade = sum_grade / (len(self.point_text) - int(empty_grade))
        if len(self.point_text) - int(empty_point) != 0:
            avg_point = sum_point / (len(self.point_text) - int(empty_point))
        if sum_point is None:
            print('None')
        try:
            result = sum_gp / sum_grade
        except ZeroDivisionError as e:
            print('except', e)
        # print(result)
        # print(avg_point)
        # print(avg_grade)
        self.text1.setText(str(avg_point))
        self.text.setText(str(avg_grade))
        self.text2.setText(str(result))

    def show_about_dialog(self):
        about_text = "<center>这是一个简易的GPA计算器</center><p>版本1.0</p><p>@Author：LZY</p><p>@gitbub：love-in-cpp</p>"
        QMessageBox.about(self, '说明', about_text)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    gpa = GPA_calculator()
    gpa.show()
    sys.exit(app.exec_())
