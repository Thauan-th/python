class Singleton:
        def __new__(cls) -> object:
                if not hasattr(cls, 'instance'):
                        cls.instance = super().__new__(cls)
                return cls.instance


s1 = Singleton()

print(id(s1))

s2 = Singleton()

print(id(s2))

same_id = id(s1) == id(s2)
print(same_id)
