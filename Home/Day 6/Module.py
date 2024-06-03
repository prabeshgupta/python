#Module is code library. A file containing set of functions that you can use in your applications.

# Import module and provide alias
import ModuleDemo as md

#Built in module
import platform

#To import a part of a module
from ModuleDemo import person

md.demo(10)

print(len(md.person))


#Built in module

x = platform.system()
print(x)


#Part of module
print(person)