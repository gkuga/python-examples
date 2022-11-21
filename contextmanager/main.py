class MyContextManager:
    def __enter__(self):
        print('enter')
        return 'return value'

    def __exit__(self, *args):
        print('exit')


with MyContextManager() as cm:
    print(cm)
    print('end')
