import seldom
from selenium import webdriver



if __name__ == '__main__':
    seldom.main(path="./test_dir/test_gl_login.py",
                browser="chrome",
                title="格力测试",
                description="测试环境：Chrome 80.0.0",
                rerun=0,
                save_last_run=False
                )

'''
说明：
path ： 指定测试目录。
browser: 指定浏览，默认chrome。
title ： 指定测试项目标题。
description ： 指定测试环境描述。
debug ： debug模式，设置为True不生成测试用例。
rerun ： 测试失败重跑
'''