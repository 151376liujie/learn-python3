import logging
from util import printMsg

root = logging.getLogger()
root.setLevel(logging.INFO)

# 创建handler
fh = logging.FileHandler("test.log", encoding="utf-8")
ch = logging.StreamHandler()


# 设置输出日志格式
formatter = logging.Formatter(
    fmt="%(asctime)s %(name)s %(filename)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %X"
)

# 为handler指定输出格式
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 为logger添加的日志处理器
root.addHandler(fh)
root.addHandler(ch)

if __name__ == '__main__':

    logger = logging.getLogger(__name__)
    logger.info("hello,man")
    logger.warning("watch out! man")
    printMsg("hello,woman")
