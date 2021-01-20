import os
import socket


def start(host, port):
    # 创建 sockets 对象
    serversocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    serversocket.bind((host, port))
    serversocket.listen()
    print("========开始接收请求===========")
    while True:
        print("开始等待新链接....")
        client, addr = serversocket.accept()
        print("连接地址: %s" % str(addr))
        while True:
            print("接受新命令~~~")
            cmd = client.recv(1024).decode(encoding="utf-8")
            print("receive message : [%s] from client: %s" % (cmd, addr))
            if not cmd:
                break
            try:
                cmd_res = os.popen(cmd).read()
            except Exception as e:
                print("cmd execute error...")
                cmd_res = "cmd error: %s" % str(e)
            if len(cmd_res) == 0:
                # 伪造一个响应，为了不让客户端卡住
                cmd_res = "cmd error."
            cmd_res_encode = cmd_res.encode(encoding="utf-8")
            print("命令执行的大小为: %d" % len(cmd_res_encode))
            # 先发送响应内容的大小给客户端
            client.send(str(len(cmd_res_encode)).encode(encoding="utf-8"))
            # 接受客户端的ack确认
            client_ack = client.recv(1024)
            # 发送数据
            client.send(cmd_res_encode)
        client.close()


if __name__ == '__main__':
    start("localhost", 9999)
