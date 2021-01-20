import socket

# logging.basicConfig()

encoding = "utf-8"


def connect(host, port):
    # 创建 sockets 对象
    client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    client_socket.connect((host, port))
    print("========开始发送请求===========")
    while True:
        cmd = input("input your request:").strip()
        if len(cmd) == 0:
            continue
        if cmd == 'quit' or cmd == 'QUIT':
            print("关闭连接....")
            client_socket.close()
            break

        count = client_socket.send(cmd.encode(encoding=encoding))
        print("请求已发送个数：%d,等待响应" % count)
        received_byte_count = 0
        received_data = bytearray()
        # 先接受服务端返回的内容大小
        total_response_count = client_socket.recv(1024).decode(encoding=("%s" % encoding))
        print("接收服务端返回数据大小: [%s]" % total_response_count)
        # ack确认收到服务端发送的命令执行的大小
        client_socket.send(b'ack')
        print("ack 服务端发送的响应大小。。。")
        while received_byte_count < int(total_response_count):
            msg = client_socket.recv(1024)
            received_byte_count += len(msg)
            received_data.extend(msg)
            print("received byte count: %d" % received_byte_count)
        else:
            print("接收到的响应消息大小为：%d,内容为: \n%s" % (len(received_data), received_data.decode(encoding=encoding)))


if __name__ == '__main__':
    connect("localhost", 9999)
