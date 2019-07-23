class Student:
    def __init__(self, name):
        self.name = name

    def sayHello(self):
        print("hello %s" % self.name)


if __name__ == '__main__':
    stu = Student('zhangsan')
    stu.sayHello()
