import hmac
import base64
from hashlib import sha256

if __name__ == '__main__':

    for i in range(2, 2):
        print(i)

    print(pow(-5, 0.5))
    appsecret = "1234".encode('utf-8')  # 秘钥
    data = "xxxxx".encode('utf-8')  # 加密数据
    print(type(appsecret))
    signature = base64.b64encode(hmac.new(appsecret, data, digestmod=sha256).digest())
    print(signature)
    # 获取十六进制加密数据
    signature = base64.b64encode(hmac.new(appsecret, data, digestmod=sha256).hexdigest().encode(encoding="utf-8"))
    print(signature)
