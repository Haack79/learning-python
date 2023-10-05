# tracebacks for exceptions raised in the application are handled here
try:
    int("N/A")
    d = {}
    d["N/A"]
except ValueError as e:
    print("could not convert string to integer: ", e)
except KeyError as e:
    print("key does not exist: ", e)
finally:
    print(
        "this will always run"
    )  # this will always run no matter what good place for cleanup code


# can have multiple except blocks for different types of errors to make it more explicit what the error is
# except blocks are run in order from top to bottom and the first one that matches the error is the one that is run - so if you have a more specific error first and a more general error second, the more specific error will never run because the more general error will catch it first
# dont catch baseEcxeption - it will catch everything and you wont know what the error is - it will catch all errors including KeyboardInterrupt and SystemExit
# can make custom exceptions by inheriting from the Exception class
# can use the raise keyword to raise an exception  - raise Exception("something went wrong")
class MyCustomError(Exception):
    pass
