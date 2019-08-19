
import random

import requests
from django.core.cache import cache

# 生成随机验证码
def get_vcode():
    vcode = ""
    for i in range(6):
        vcode += str(random.randint(0, 9))

    return vcode

# 发送短信给手机
# @shared_task
def send_sms(phone):
    YZX_SMS_URL = 'https://open.ucpaas.com/ol/sms/sendsms'
    YZX_SMS_SID = 'ef8c3118f5d87f98a0e74a1270b25f10'
    YZX_SMS_TOKEN = 'f8d54a9d5a694aaafde0da3d632f3cb6'
    YZX_SMS_APPID = '0eb5b6aa08a04e198d9b81c52b680737'
    YZX_SMS_TEMPLATE_ID = '494867'

    # 数字验证码
    vcode = get_vcode()

    # 定义请求的数据
    data = {
        "sid": YZX_SMS_SID,
        "token": YZX_SMS_TOKEN,
        "appid": YZX_SMS_APPID,
        "templateid": YZX_SMS_TEMPLATE_ID,
        "param": vcode,  # 验证码
        "mobile": phone,  # 手机号
    }

    # 发起数据
    response = requests.post(YZX_SMS_URL, json=data)
    # url 请求的地址
    # headers 请求头部
    # data 请求的数据

    # 设置缓存
    cache.set(phone, vcode, 180)

    # print(response.content.decode())
    # print(response.text)
    return vcode  # 响应数据