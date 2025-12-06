#!/usr/bin/env python
# coding:utf-8

from collections import OrderedDict
from hashlib import sha256
import hmac
from utill.get_orderNum import get_orderNum as go
from config.env import merchantID

def sortParam(key):
    print("======================================")
    print(key)
    orderNum = go()
    di = OrderedDict()
    di['amount'] = "2.2"
    di['merchantID'] = merchantID
    di['payType'] = "6"
    di['merchantOrderId'] = orderNum
    di['productName'] = "googd"
    di['productDescription'] = "apple mobile phone X7"
    di['merchantUserId'] = "u_0001"
    di['merchantUserName'] = "hello"
    # di['merchantUserEmail'] = "aab0@gmail.com"
    di['merchantUserCitizenId'] = "EHFGA5967A"
    di['redirectUrl'] = "http://kosin.free.idcfengye.com/test/prepay/callback"
    di['merchantUserDeviceId'] = "002989-93838-838848-94949"
    di['merchantUserIp'] = "192.168.1.1"
    di['countryCode'] = "IN"
    di['currency'] = "INR"

    dic1SortList = sorted( di.items(),key = lambda item: item[0],reverse = False)

    print(dic1SortList)
    param=[]
    for i in dic1SortList:
        param.append(i[1])
    param.append(key)
    print(param)
    result = ",".join(param)
    print(result)
    r=result.replace(",","")
    # print(r)
    return r

@sortParam
def get_sign(func):
    def wapper(key):
        print("++++++++++++++++++++++++++++++++++++")
        print(key)
        signStr = func(key)
        message = signStr.encode('utf-8')
        key = key.encode('utf-8')

        # print(type(message))
        signH = hmac.new(key, message, digestmod=sha256).hexdigest().encode(encoding="utf-8")
        # print(signH)
        bs = str(signH, 'utf-8')
        signN = bs.upper()
        return signN
    return wapper





if __name__ == '__main__':
    key = "34531832-2a6f-4246-961b-00cf05e4085f"
    get_sign(key)