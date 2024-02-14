class Singleton:
    __instance = None

    def __init__(self) -> None:
        if self.__instance is None:
            print("No instance")
        else:
            print(f"Instace: {id(self.get_instance())}")

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = Singleton()
        return cls.__instance


c1 = Singleton()  # No instance yet

print(f"New instance: {Singleton.get_instance()}")  # Creating new instance

c2 = Singleton()  # should have an instance
