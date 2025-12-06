class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Human):
    def __init__(self, name, age, score, clazz):
        super().__init__(name, age)
        self.score = score
        self.clazz = clazz

    def print_score(self):
        print('学生姓名：%s\n学生年龄：%s\n学生班级：%s\n学生分数：%s' % (self.name, self.age, self.clazz, self.score))

st1 = Student("刘若熙", 11, 90, '四年级2班')
st1.print_score()
