import hashlib
import json
import logging
import os
import socket

logging.basicConfig(format='%(name)s %(levelname)s %(pathname)s %(lineno)d %(asctime)s %(funcName)s: %(message)s',
                    level=logging.INFO)

from cmdException import CmdException

logger = logging.getLogger(__name__)


class FtpServer(object):

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.socket.listen()

    def interactive(self):
        logger.info("========开始接收请求===========")
        while True:
            logger.info("开始等待新链接....")
            client, addr = self.socket.accept()
            logger.info("请求来自: %s", str(addr))
            self._process_request(client, addr)
            client.close()

    def _process_request(self, client, addr):
        while True:
            logger.info("接收新命令~~~")
            data = client.recv(1024).decode(encoding="utf-8")
            logger.info("receive message : [%s] from client: %s", data, addr)
            if not data:
                break
            request = None
            try:
                request = json.loads(data)
                if not hasattr(self, "_cmd_%s" % request["action"]):
                    continue
                func = getattr(self, "_cmd_%s" % request["action"])
                func(request, client)
            except CmdException as cmdException:
                logger.warning("cmd: [%s] error... msg: [%s]", request["action"], cmdException.message)
                client.send(str(cmdException).encode(encoding="utf-8"))
            except Exception as e:
                logger.error("cmd execute error... %s", e)
                cmd_res = "cmd error: %s" % str(e)
                client.send(cmd_res.encode(encoding="utf-8"))
                break

    def _cmd_get(self, request, client):
        if not os.path.isfile(request["filename"]):
            raise CmdException(500, "invalid command, [%s] is not file" % request["filename"])
        filesize = os.path.getsize(request["filename"])
        logger.info("文件: [%s]的大小为: [%d]", request["filename"], filesize)
        # 发送文件大小
        client.send(str(filesize).encode(encoding="utf-8"))
        # 接受客户端ack消息
        client_ack = client.recv(1024)
        logger.info("客户端ack: %s", client_ack)
        md5 = hashlib.md5()
        with open(request["filename"], mode='rb') as f:
            for line in f:
                # 发送文件数据
                client.send(line)
                # 计算md5值
                md5.update(line)
        # 发送文件的md5
        hexdigest = md5.hexdigest()
        logger.info("发送给客户端文件md5：%s", hexdigest)
        client.send(hexdigest.encode(encoding="utf-8"))

    def _cmd_put(self, request, client):
        # put /Users/liujie/PycharmProjects/learn-python/sockets/socket_ssh_server.py 1986572
        # 发送ack确认
        client.send("ack".encode(encoding="utf-8"))
        filesize = request["filesize"]
        received_byte_count = 0
        with open(file=request["filename"], mode='wb') as f:
            while received_byte_count < filesize:
                msg = client.recv(1024)
                received_byte_count += len(msg)
                f.write(msg)
            else:
                logger.info("文件接收完毕，共写入:[%d], 文件大小:[%d]", received_byte_count, filesize)


if __name__ == '__main__':
    ftpServer = FtpServer("localhost", 9999)
    ftpServer.interactive()
