def decorator_for_annotation(func):
    def returned_function():
        print("additional logic")
        func()
    return returned_function

@decorator_for_annotation
def my_name():
    print('Anastasia')

my_name()


# additional logic
# Anastasia


