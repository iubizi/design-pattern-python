class apple(object):
    # apple
    def __repr__(self):
        return 'apple factory'

class bnana(object):
    # bnana
    def __repr__(self):
        return 'bnana factory'



import abc

class AbstractFactory(object):
    # 抽象工厂
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def product_fruit(self):
        pass

class apple_factory(AbstractFactory):
    # apple工厂（重写方法）
    def product_fruit(self):
        return apple()

class banana_factory(AbstractFactory):
    # banana工厂（重写方法）
    def product_fruit(self):
        return bnana()

fruit_1 = apple_factory().product_fruit()
fruit_2 = banana_factory().product_fruit()

print(fruit_1)
print(fruit_2)
