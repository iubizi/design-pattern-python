class apple(object):
    # apple
    def __repr__(self):
        return 'apple factory'

class bnana(object):
    # bnana
    def __repr__(self):
        return 'bnana factory'

class simple_factory(object):
    # 简单工厂模式
    @staticmethod
    def product_fruit(name):
        if name == 'a':
            return apple()
        elif name == 'b':
            return bnana()

fruit_1 = simple_factory.product_fruit('a')
fruit_2 = simple_factory.product_fruit('b')

print(fruit_1)
print(fruit_2)
