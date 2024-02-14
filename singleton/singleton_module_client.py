import singleton_module

print(singleton_module.P)
print(singleton_module.do_something())
print(singleton_module.is_ok())

import singleton_module as sm

print(sm.P)
print(sm.is_ok(True))
print(sm.do_something())


# Python handles like Singletons - avoiding multiples instances from the same module
