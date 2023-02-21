import traceback

is_html = lambda f: f.endswith('.html') or \
                    f.endswith('.htm') or \
                    f.endswith('.xhtml')

def safe(default=None):
    def wrapper(func):
        def inner(*args, **kw):
            try: return func(*args, **kw)
            except: traceback.print_exc()
        return inner
    return wrapper