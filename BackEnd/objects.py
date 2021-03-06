from ClearmindBase import Server
from flask_socketio import SocketIO
from typing import Dict, Tuple
from random import randint
from .logger import Logger

import sys
sys.path.append("..")
# from ..ClearmindBase import Server

clearmind_socketio = SocketIO()
cookie_user_dict: Dict[str, Tuple[str, float]] = {}
user_cookie: Dict[str, str] = {}

DISCONNECT_TIME = 300

# 等待时间
# 地图的创建, 1000 x 1000 大概需要10秒左右,  一般地图大小使用300 x 300 足够
SERVER_WAIT_TIME = 20 # 搁置 


CM_server = Server()
CM_logger = Logger()

def print_and_log(data):
    data = str(data)
    print(data)
    CM_logger.log(data)

def gen_cookie():
    '''通过随机数得到一个身份标识码, 重复的识别标识码应该在调用完次函数后判断'''
    cookie = randint(10000000000000000000, 9999999999999999999999999)
    while True:
        if cookie not in cookie_user_dict:
            break
        cookie = randint(10000000000000000000, 9999999999999999999999999)
    return cookie
