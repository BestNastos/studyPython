# import this
import study

print(study.name)
study.printName()

study.printName = lambda : print("Redefined printName function")

study.printName()