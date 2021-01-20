import hashlib
import json
import logging
import os
import socket
import time

import util
from cmdException import CmdException
from protocol import CMD_ERROR_MARK

logging.basicConfig(format='%(name)s %(levelname)s %(pathname)s %(lineno)d %(asctime)s %(funcName)s: %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

encoding = "utf-8"


class FtpClient(object):
    """
    ftp 文件服务器 客户端类
    """

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.socket.connect((host, port))

    def help(self):
        logger.info("""------------------------------------------------
        cmd list:
            [put localfile remotepath] 
            [get filename]
            [ls  list current directory]
            [pwd print user work dir]
            [auth username password]
------------------------------------------------""")

    def interactive(self):
        logger.info("========开始发送请求===========")
        while True:
            self.help()
            cmd = input("input your command =>: ").lower().strip()
            if len(cmd) == 0:
                continue
            if cmd in ['quit', 'exit']:
                logger.info("bye bye....")
                self.socket.close()
                break
            cmd_str = cmd.split()
            if not hasattr(self, "_cmd_%s" % cmd_str[0]):
                continue
            func = getattr(self, "_cmd_%s" % cmd_str[0])
            try:
                func(*cmd_str)
            except CmdException as cmd_err:
                logger.warning("cmd: [%s] error. msg: %s", cmd_str[0], str(cmd_err))
                if cmd_err.send:
                    self.socket.send(cmd_err.message.encode("utf-8"))
            except Exception as e:
                logger.error("func: [%s] execute error. error msg: %s", func, str(e))
                self.socket.close()
                break

    def _cmd_auth(self, *args):
        """
        认证授权
        :param args:
        :return:
        """
        if len(args) != 3:
            raise CmdException(400, "invalid command length, required 3 but actual is:[%d]" % len(args), False)
        request = {
            "action": "auth",
            "filename": args[1]
        }
        # TODO

    def _cmd_get(self, *args) -> None:
        """
        下载远端文件到本地

        get remotefile localpath
        :param filepath: 要下载的文件
        :param target_path: 保存到本地的路径
        :return: None
        """
        if len(args) != 3:
            raise CmdException(400, "invalid command length, required 3 but actual is:[%d]" % len(args), False)
        # targetPath就不往服务端发了，因为服务端用不到，而且还可以减少数据发送量
        request = {
            "action": "get",
            "filename": args[1]
        }
        count = self.socket.send(json.dumps(request).encode(encoding="utf-8"))
        logger.info("请求已发送个数：%d,等待响应", count)
        received_byte_count = 0
        buffer_size = 1024
        # 先接受服务端返回的内容大小
        total_response_count = self.socket.recv(buffer_size).decode(encoding=encoding)
        if total_response_count.find(CMD_ERROR_MARK) != -1:
            exception = json.loads(total_response_count)
            logger.warning("检测到异常信息: [%s]", total_response_count)
            # 错误信息不发送给对方
            raise CmdException(exception["code"], exception["message"], False)
        logger.info("返回的文件大小: [%s]", total_response_count)
        # ack确认收到服务端发送的命令执行的大小
        self.socket.send(b'ack')
        logger.info("ack 服务端发送的响应大小。。。")
        m = hashlib.md5()
        total_response_count = int(total_response_count)
        start = time.time()
        with open(file=args[2], mode='wb') as f:
            while received_byte_count < total_response_count:
                # 按需接收
                byte_delta = total_response_count - received_byte_count
                # 说明只需要接收一次
                if byte_delta <= buffer_size:
                    buffer_size = byte_delta
                msg = self.socket.recv(buffer_size)
                received_byte_count += len(msg)
                f.write(msg)
                m.update(msg)
                util.show_processing_bar(received_byte_count, total_response_count)
            else:
                logger.info("接收到的响应消息大小为：%d", received_byte_count)
                # 接收文件的MD5值
                md5 = self.socket.recv(buffer_size).decode(encoding="utf-8")
                end = time.time()
                logger.info("文件传输完毕，共耗时: %f", (end - start))
                logger.info("原文件md5值为   :%s,接收文件md5值为 :%s", md5, m.hexdigest())

    def _cmd_put(self, *args):
        """
        上传本地文件到远端
        put localfile remotepath
        :param filepath: 要上传的文件
        :param remote_path: 远端存放文件的路径
        :return: None
        """

        if len(args) != 3:
            raise CmdException(400, "invalid command length, required 3 but actual is:[%d]" % len(args), False)
        if not os.path.isfile(args[1]):
            raise CmdException(400, "invalid command, [%s] is not file:" % args[1], False)
        filesize = os.path.getsize(args[1])
        request = {
            "action": "put",
            "filename": args[2],
            "filesize": filesize
        }
        logger.info("发送命令给服务端:[%s]", request)
        self.socket.send(json.dumps(request).encode(encoding))
        ack = self.socket.recv(1024)
        already_send = 0
        with open(file=args[1], mode='rb') as f:
            for line in f:
                # 发送文件内容
                already_send += self.socket.send(line)
                util.show_processing_bar(already_send, filesize)
            else:
                logger.info("文件发送完毕")


if __name__ == '__main__':
    ftpClient = FtpClient("localhost", 9999)
    ftpClient.interactive()
