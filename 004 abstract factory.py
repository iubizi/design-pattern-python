class apple(object):
    # apple
    def __repr__(self):
        return 'apple factory'

class bnana(object):
    # bnana
    def __repr__(self):
        return 'bnana factory'

class apple_juice(object):
    # apple juice
    def __repr__(self):
        return 'apple juice factory'

class banana_juice(object):
    # bnana juice
    def __repr__(self):
        return 'bnana juice factory'



import abc

class AbstractFactory(object):
    # 抽象工厂
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def product_fruit(self):
        pass

    @abc.abstractmethod
    def product_jucie(self):
        pass

class apple_factory(AbstractFactory):
    # apple工厂（重写方法）
    def product_fruit(self):
        return apple()

    def product_juice(self):
        return apple_juice()

class banana_factory(AbstractFactory):
    # banana工厂（重写方法）
    def product_fruit(self):
        return bnana()

    def product_juice(self):
        return banana_juice()



fruit_1 = apple_factory().product_fruit()
fruit_2 = banana_factory().product_fruit()

print(fruit_1)
print(fruit_2)

juice_1 = apple_factory().product_juice()
juice_2 = banana_factory().product_juice()

print(juice_1)
print(juice_2)
