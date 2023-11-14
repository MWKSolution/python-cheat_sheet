import sys
from custom_traceback import compact_tb


def func_func_func():
    x = 1 / 0


def func_func():
    try:
        func_func_func()
    except Exception as exc:
        raise AttributeError('error in func_func') from exc


def func():
    try:
        func_func()
    except Exception as exc:
        raise NameError('error in func') from exc


def main():

    func()


if __name__ == '__main__':
    sys.excepthook = compact_tb.exception_hook
    main()
