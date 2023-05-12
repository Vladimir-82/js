from functools import wraps


def retry(times):
    def decorator(func):
        @wraps(func)
        def surrogate(*args, **kwargs):
            for i in range(times):
                try:
                    func(*args, **kwargs)
                except Exception:
                    pass
                else:
                    raise Exception('MaxRetriesException')
            else:

                return func(*args, **kwargs)
        return surrogate
    return decorator


@retry(3)
def no_way():
    raise ValueError


try:
    no_way()
except Exception as e:
    print(type(e))