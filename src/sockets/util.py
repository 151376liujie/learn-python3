import math
import sys


def show_processing_bar(received_byte_count, total_response_count):
    """
         total 总数据大小，portion 已经传送的数据大小
         :param received_byte_count: 已经接收的数据量
         :param total_response_count: 总数据量
         :return: 接收数据完成，返回True
    """

    part = total_response_count / 50  # 1%数据的大小
    count = math.ceil(received_byte_count / part)
    sys.stdout.write('\r')
    sys.stdout.write(('[%-50s] %.2f%%' % (('>' * count), received_byte_count / total_response_count * 100)))
    sys.stdout.flush()
    if received_byte_count >= total_response_count:
        sys.stdout.write('\n')
    return True
