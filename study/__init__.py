print ("__init__")

# этот модуль запустится при выполнении импортов
# здесь тоже можно прописать импорты:

from .ImportThisToTestImports import *

# и теперь в другом файле можно иметь доступ к переменным модулей по имени пакета study, например как в модуле study2:

#import study
#print(study.name)

# а что если в 2х импортированных модулях есть переменные с одинаковым имененм?
# - тогда нужно будет все же еще указывать и название модуля перед переменной тоже

# from .study3 import printName # -> doesn't work,
# will not be able to make call to printName() without writing the following line in imports in module:
# from study.study3 import printName