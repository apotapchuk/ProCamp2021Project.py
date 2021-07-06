import time
import functools


def decorator_wait(func):
    @functools.wait(func)
    def wait(method, error=Exception, timeout=10, interval=0.5, check=False, **kwargs):
        st = time.time()
        while time.time() - st < timeout:
            try:
                result = method(**kwargs)
                if check:
                    if result:
                        return result
                    last_exception = f'Method {method, __name__} returned {result}'
                else:
                    return result
            except error as error:
                last_exception = error
                time.sleep(interval)
            raise TimeoutError(f'Method {method, __name__} timeout in {timeout} sec with exception: "{last_exception}"')
