import socket

# 创建 sockets 对象
serversocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

serversocket.bind(("localhost", 9999))
serversocket.listen(2)
print("========开始接收请求===========")
while True:
    print("开始等待新链接....")
    client, addr = serversocket.accept()
    print("连接地址: %s" % str(addr))
    while True:
        msg = client.recv(1024).decode(encoding="utf-8")
        print("receive message : [%s] from client: %s" % (msg, addr))
        if not msg:
            break
        client.send(("response to client :%s" % msg.upper()).encode(encoding="utf-8"))
    client.close()
