'''
Create exceptions based on your inputs. Please follow the tasks below.

 - Capture and handle system exceptions
 - Create custom user-based exceptions
'''


class CustomInputError(Exception):
    def __init__(self, *args, **kwargs):
        print("Going through my own CustomInputError")
        # Exception.__init__(self, *args, **kwargs)


class MyZeroDivisionException(ZeroDivisionError):
    def __init__(self):
        print("The data is not valid")


class DataNotValidException(TypeError):
    def __init__(self):
        print("The data contains Strings. Only numbers are expected in the input data")
