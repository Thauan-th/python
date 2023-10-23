class Singleton:
    __state = {}
    
    def __new__(cls, *args, **kwargs):
        obj = super(Singleton, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__state
        return obj


m1 = Singleton()
m2 = Singleton()
print(f'm1: {id(m1)}')
print(f'm2: {id(m2)}')

m1.name = 'Thauan'

# Using the same state on both classes

print(m1.__dict__)
print(m2.__dict__)
