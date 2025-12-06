def decorate(func):
    def wrapper(*args, **kwargs):
        print("==========执行前==========")
        func(*args, **kwargs)
        print("==========执行后==========")

    return wrapper


@decorate
def hello(*args, **kwargs):
    print(args)
    print(kwargs)


li = [1, 2, 3, 4]
kw = {"a": 1, "b": 2}
hello(*li, **kw)
