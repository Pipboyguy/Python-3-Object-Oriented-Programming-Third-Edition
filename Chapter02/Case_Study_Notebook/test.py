class MyClass:
    global hh
    def __init__(self):
        pass

    def method(self):
        hh = 2
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls


    @staticmethod
    def staticmethod():
        return 'static method called'
