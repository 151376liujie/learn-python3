import turtle

# 绘制一条蟒蛇
turtle.setup(650, 350, 200, 200)
# 抬起画笔
turtle.penup()
# 后退250像素
turtle.fd(-250)
# 画笔落下
turtle.pendown()
# 设置画笔大小
turtle.pensize(25)
# 设置画笔颜色
turtle.pencolor("purple")
# 设置海龟角度为朝向-40°
turtle.seth(-40)

for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
# 设置海龟在以40像素为半径前进80/2角度
turtle.circle(40, 80 / 2)
# 让海龟前进40像素
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2 / 3)
turtle.done()
