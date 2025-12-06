import pymysql

pymysql.install_as_MySQLdb()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, DateTime

Base = declarative_base()
engine = create_engine('mysql://%s:%s@%s/%s?charset=utf8&autocommit=true' %
                       ("root", "root", "localhost", "test"),
                       encoding='utf-8', echo=False,
                       pool_size=100, pool_recycle=10)
DB_Session = sessionmaker(bind=engine, autocommit=True)
session = DB_Session()


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer(), primary_key=True)
    name = Column(String(255))
    age = Column(String(255))
    create_date_time = Column(DateTime())


if __name__ == '__main__':
    students = session.query(Student).filter(Student.name == None, Student.id == 100, Student.age == 30).all()
    for index, student in enumerate(students):
        print(student.name, student.age, student.create_date_time)
