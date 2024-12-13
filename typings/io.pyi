"""
Module: 'io' on micropython-v1.20.0-preview-esp32
"""
# MCU: {'family': 'micropython', 'version': '1.20.0-preview', 'build': '696', 'ver': '1.20.0-preview-696', 'port': 'esp32', 'board': '', 'cpu': 'ESP32S3', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Generator
from _typeshed import Incomplete

def open(*args, **kwargs) -> Incomplete:
    ...


class IOBase():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class BytesIO():
    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def seek(self, *args, **kwargs) -> Incomplete:
        ...

    def getvalue(self, *args, **kwargs) -> Incomplete:
        ...

    def tell(self, *args, **kwargs) -> Incomplete:
        ...

    def flush(self, *args, **kwargs) -> Incomplete:
        ...

    def readline(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class StringIO():
    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def seek(self, *args, **kwargs) -> Incomplete:
        ...

    def getvalue(self, *args, **kwargs) -> Incomplete:
        ...

    def tell(self, *args, **kwargs) -> Incomplete:
        ...

    def flush(self, *args, **kwargs) -> Incomplete:
        ...

    def readline(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class BufferedWriter():
    def flush(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

