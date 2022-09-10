def help(**kwargs):
    def decorator(func):
        func.__help__ = kwargs
        return func