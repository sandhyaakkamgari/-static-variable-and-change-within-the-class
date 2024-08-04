class MyClass:
    class_variable = 10  # This is a class variable

    def __init__(self):
        pass

    @classmethod
    def change_class_variable(cls, new_value):
        cls.class_variable = new_value

print(MyClass.class_variable)

MyClass.change_class_variable(20) 

print(MyClass.class_variable)