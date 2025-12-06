import turtle
import time

"""
    绘制七段数码管
"""
def drawLine(draw):
    """
    绘制一条线，并向右转90度
    :param draw: 是否绘制线条的标识
    :return:
    """
    if draw:
        turtle.pendown()
    else:
        turtle.penup()
    turtle.fd(40)
    turtle.right(90)


def drawDigit(digit):
    """
    绘制一个数字
    :param digit: 数字
    :return:
    """
    drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 6, 8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)


def drawDate(date):
    for digit in date:
        drawDigit(int(digit))


def main():
    # date = input('请输入你要绘制的时间：')
    date = time.strftime("%Y%m%d")
    print(date)
    turtle.pensize(5)
    turtle.pencolor("gray")
    turtle.penup()
    turtle.forward(-300)
    drawDate(date)
    turtle.hideturtle()
    turtle.done()


main()
