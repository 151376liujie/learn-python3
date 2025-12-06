import turtle


def drawKoch(size, n):
    """
    绘制n阶科赫曲线
    :param size: 线段的长度
    :param n: 阶数
    :return:
    """
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            drawKoch(size / 3, n - 1)


def main():
    n = input("请输入绘制科赫雪花算法的阶数:")
    turtle.setup(600, 600)
    turtle.pensize(2)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pencolor("green")
    turtle.pendown()

    level = 3

    drawKoch(400, level)
    turtle.right(120)

    drawKoch(400, level)
    turtle.right(120)

    drawKoch(400, level)
    turtle.right(120)

    turtle.hideturtle()
    turtle.done()


main()
