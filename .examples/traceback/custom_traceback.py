import sys
from pathlib import Path
from linecache import getline
from typing import Generator, TextIO, Type
from types import TracebackType


class CustomTraceback:
    """
    Helper class for traceback handling. Doesn't create any instances of itself!!!
    General info:
    It goes down exceptions chain and gets traceback for each exception than format string with that.
    Usage:
    CustomTraceback(exc) -> get exception formatted string
    CustomTraceback.print_exception(exc, file) -> print formatted exception to file (stdout, stderr, ...)
    CustomTraceback.exception_hook -> to be used with sys.excepthook
    """
    STDERR = sys.stderr  # get the standard error object

    def __new__(cls, exc: BaseException) -> str:
        """
        Doesn't create instances. Returns formatted exception string.
        :param exc: exception
        :return: formatted exception string
        """
        return cls.format_exception(exc)

    @classmethod
    def get_exception_chain(cls, exc: BaseException) -> Generator[BaseException, None, None]:
        """
        Get exception chain starting from given exception (exc) -  as generator
        Neet to be reversed to got most last exception at the end.
        :param exc: exception
        :return: iterable exception chain
        """
        while True:
            yield exc
            exc = exc.__context__
            if not exc:
                break

    @staticmethod
    def format_traceback(tb: TracebackType, code: bool = True) -> str:
        """
        Format traceback string
        :param tb: traceback
        :param code: if code line where exception occurred should be included
        :return: formatted traceback string
        """
        tb_str = '| '
        while tb is not None:
            file = tb.tb_frame.f_code.co_filename
            file_name = Path(file).stem
            func_name = tb.tb_frame.f_code.co_name
            line = getline(file, tb.tb_lineno).strip()
            # only raise, exception description is printed at the end
            line = (' "raise"' if line.startswith('raise') else f' "{line}"') if code else ''
            line_no = str(tb.tb_lineno)
            tb = tb.tb_next
            tb_str += f'{file_name}::{func_name} @{line_no}{line} | '
        return tb_str

    @classmethod
    def format_exception(cls, exc: BaseException, reverse: bool = False) -> str:
        """
        Format exception string
        :param exc: exception
        :param reverse: Neet to be reversed to got most last exception at the end.
        :return: formatted exception string
        """
        chain = tuple(cls.get_exception_chain(exc))
        if reverse:
            chain = reversed(chain)
        exc_str = '\n'.join(f'{cls.format_traceback(e.__traceback__)}>> {type(e).__name__}: {str(e)}.' for e in chain)
        return exc_str

    @classmethod
    def print_exception(cls, exc: BaseException, file: TextIO = STDERR) -> None:
        """
        Just print formatted exception to the given io object (stdout, stderr, ...)
        :param exc: exception
        :param file: io object file
        :return: None
        """
        print(cls.format_exception(exc), file=file)

    @classmethod
    def exception_hook(cls, exc_type: Type, exc_value: BaseException, trace_back: TracebackType) -> None:
        """
        Method to be used as system exception hook:
        sys.excepthook = CustomTraceback.exception_hook
        :param exc_type: exc_hook signature
        :param exc_value: exc_hook signature
        :param trace_back: exc_hook signature
        :return: None
        """
        print('Error:', file=cls.STDERR)
        cls.print_exception(exc_value, file=cls.STDERR)


compact_tb = CustomTraceback
