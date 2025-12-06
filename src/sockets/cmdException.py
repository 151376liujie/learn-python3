import json
import logging
from protocol import CMD_ERROR_MARK

class CmdException(Exception):

    def __init__(self, code, message, send=True):
        """
        构造函数
        :param sendToServer: 是否发送错误信息给服务端
        :param message: 错误信息
        """
        self.code = code
        self.send = send
        if message.startswith(CMD_ERROR_MARK):
            self.message = message
        else:
            self.message = CMD_ERROR_MARK + message

    def __str__(self):
        return json.dumps({
            "code": self.code,
            "message": self.message,
            "send": self.send
        })


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    exception = CmdException(400, "erorr", False)
    logger.warning(str(exception))

    logger.info(type(json.loads(str(exception))))
