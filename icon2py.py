# -*- coding = utf-8 -*-
# @Time : 2021/7/12 17:16
# @Author : 刘正阳
# @File : icon2py.py
# @Software : PyCharm

import base64

open_icon = open("成绩分析.png", "rb")
b64str = base64.b64encode(open_icon.read())
open_icon.close()
write_data = write_data = "img = %s" % b64str
f = open("icon.py", "w+")
f.write(write_data)
f.close()
