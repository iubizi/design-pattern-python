class people:
    name = ''
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def reveal(self):
        print('=== people ===')
        print('name =', self.name)
        print('age =', self.age)
        print()

# 基类测试
basic_test = people(name='Tom', age=23)
basic_test.reveal()



class student(people):
    gpa = 0

    def __init__(self, name, age, gpa):
        people.__init__(self, name, age)
        self.gpa = gpa
    """
    def reveal(self):
        print('=== student ===')
        print('name =', self.name)
        print('age =', self.age)
        print('gpa =', self.gpa)
        print()
    """

# 继承测试
inherit_test = student(name='ken', age=16, gpa=3.0)
inherit_test.reveal()
