try:
    2/0
except ZeroDivisionError as e:
    print("Exception: " + str(e))
finally:
    print("finally")

try:
   raise Exception("Some exception")
except Exception as e:
   print("Exception: " + str(e))