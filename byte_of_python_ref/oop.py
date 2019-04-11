#!/usr/bin/env python

# self

# self - указывает на сам объект экземпляра класса. Добавляется к началу списка параметров метода класса
# Пример: есть класс MyClass и экземпляр класса - myobject. При вызове метода myobject.method(arg1, arg2) python
# выполнит следующую подстановку: MyClass.method(myobject, arg1, arg2)
# У любого метода ВСЕГДА есть хотябы один аргумент - self


# КЛАССЫ

# инструкция pass - указывает на пусто тело функции или класса.
# В выводе ниже: __main__ - модуль, хранящий экземпляр класса Person => __main__.Person object; at 0x033CF870 - область
# памяти, куда записан данный объект


# class Person:
#     pass
#
#
# p = Person()
# print(p) # -> <__main__.Person object at 0x033CF870>

# Методы объектов


# class Person:
#     def say_hi(self):
#         print('Hi! How are you?')
#
#
# p = Person()
# p.say_hi()

# или
# Person().say_hi()

# Метод __init__

# Метод __init__ запускается при создании объекта класса.
# Метод __init__ не вызывается явным образом, а получает аргументы, переданные при вызове класса


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def say_hi(self):
#         print('Hello! My name is', self.name)
#
#
# p = Person('Swaroop')
# p.say_hi()

# или
# Person('Swaroop').say_hi()


# Переменные класса и объекта Переменные внутри класса являются обычными переменными заключенными в пространство имен
# классов и объектов. Они доступны только в контексте данных классов или объектов

# Переменные класса разделяемы, доступ к ним могут получить все экземпляры данного класса. Переменная класса одна,
# поэтому изменение данной переменной в одном экземпляре класса отразится на всех остальных экземплярах

# Переменная объекта принадлежит только этому объекту и недоступна другим объектам. Все переменные объекта изменяются
# независимо.

# !!! Переменные класса и объекта с одинаковыми именами делают недоступными переменную класса

# Любые методы принадлежащие классу, а не объекту могут быть определены как classmethod или staticmethod. classmethod
# предоставляет информацию о том в каком классе находится, classmethod - нет

# Метод __del__ вызывается всякий раз перед уничтожением объекта.


# class Robot:
#     '''Presents the robot with name'''
#     # Переменная класса, содержащая количество роботов
#     population = 0
#
#     def __init__(self, name):
#         self.name = name
#         print('Initialization {0}'.format(self.name))
#
#         # При создании этой личносити робот добавляется к переменной 'population'
#         Robot.population += 1
#
#     def __del__(self):
#         '''I'm die'''
#         print('{0} destroyed'.format(self.name))
#
#         Robot.population -= 1
#
#         if Robot.population == 0:
#             print('{0} was the last'.format(self.name))
#         else:
#             print('{0:d} working robots rest'.format(Robot.population))
#
#     def say_hi(self):
#         '''The robot's greating
#
#         Yes, they are can do this'''
#         print('Salute! My owners call me {0}'.format(self.name))
#
#     def how_many():
#         '''Presents number of robots'''
#
#         print('There is/are {0:d} robot(s)'.format(Robot.population))
#
#     how_many = staticmethod(how_many)
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# Robot.how_many()
#
# droid2 = Robot('C-3PO')
# droid1.say_hi()
# Robot.how_many()
#
# print('It\'s time to destroy the robots')
#
# del droid1
# del droid2
#
# Robot.how_many()


# Наследование

# Базовый класс или надкласс - класс от которого происходит наследование.
# Производный класс или подкласс - класс, который наледует.

# При наследовании необходимо вызвать конструктор базового класса явно (вручную)
# BaseClass.__init__(ChildClass, arg1, ...arg_n)

# Множественное наследование - неследование от двух и более классов


# class SchoolMember:
#     '''Presents any member of the school'''
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('Created SchoolMember {0}'.format(self.name))
#
#     def tell(self):
#         '''Show the information'''
#         print('The name: {0}. The age: {1}'.format(self.name, self.age), end=" ")
#
#
# class Teacher:
#     '''Presents the teacher'''
#     def __init__(self, name, age, salary):
#         SchoolMember.__init__(self, name, age)
#         self.salary = salary
#         print('The teacher was created: {0}'.format(self.name))
#
#     def tell(self):
#         SchoolMember.tell(self)
#         print('The salary is: {0}'.format(self.salary))
#
#
# class Student:
#     '''Presents the student'''
#     def __init__(self, name, age, marks):
#         SchoolMember.__init__(self, name, age)
#         self.marks = marks
#         print('The student was created: {0}'.format(self.name))
#
#     def tell(self):
#         SchoolMember.tell(self)
#         print('The marks are: {0:d}'.format(self.marks))
#
#
# t = Teacher('Mrs Shrividia', 40, 30000)
# s = Student('Swaroop', 25, 75)
#
# members = [t, s]
#
# for member in members:
#     member.tell()


# Метаклассы

# Метаклассы можно использовать для создания новых классов. Они существуют для изменения или добавления нового поведения
# в классы

# В случае когда не нужно создание экземпля базового класса можно использовать концепцию "абстрактных классов". Такие
# классы не используются в качестве реальных классов

# Из-за того, что метод SchoolMember.tell является абстрактным, экземпляр класса SchoolMember не создается. См пример
# ниже

from abc import *


class SchoolMember(metaclass=ABCMeta):
    '''Presents any person of the school'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Created SchoolMember: {0}'.format(self.name))

    @abstractmethod
    def tell(self):
        '''Show the information'''
        print('The name: {0} The age: {1}'.format(self.name, self.age), end=' ')


class Teacher(SchoolMember):
    '''Presents the teacher'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Created the teacher: {0}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('The salary: {0:d}'.format(self.salary))


class Student(SchoolMember):
    '''Presents the student'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('Created the student: {0}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('The marks: {0:d}'.format(self.marks))


t = Teacher('Mrs Shrividia', 40, 30000)
s = Student('Swaroop', 25, 75)

members = [t, s]

for member in members:
    member.tell()