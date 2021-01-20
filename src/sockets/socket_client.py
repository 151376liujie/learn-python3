import socket

# logging.basicConfig()

# 创建 sockets 对象
client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

client_socket.connect(("localhost", 9999))
print("========开始发送请求===========")
while True:
    choice = input("input your request:")
    if not choice:
        continue
    if choice.strip() == 'quit' or choice.strip() == 'QUIT':
        print("关闭连接....")
        client_socket.close()
        break
    count = client_socket.send(choice.encode(encoding="utf-8"))
    print("请求已发送个数：%d,等待响应..." % count)
    msg = client_socket.recv(1024).decode(encoding="utf-8")
    print("接收到的响应消息为: %s" % msg)
