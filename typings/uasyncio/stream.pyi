"""
Module: 'uasyncio.stream' on micropython-v1.20.0-preview-esp32
"""
# MCU: {'family': 'micropython', 'version': '1.20.0-preview', 'build': '696', 'ver': '1.20.0-preview-696', 'port': 'esp32', 'board': '', 'cpu': 'ESP32S3', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Generator
from _typeshed import Incomplete

start_server: Generator ## = <generator>

class Stream():
    def get_extra_info(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    drain: Generator ## = <generator>
    wait_closed: Generator ## = <generator>
    readexactly: Generator ## = <generator>
    aclose: Generator ## = <generator>
    awrite: Generator ## = <generator>
    awritestr: Generator ## = <generator>
    read: Generator ## = <generator>
    readinto: Generator ## = <generator>
    readline: Generator ## = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        ...

stream_awrite: Generator ## = <generator>

class StreamReader():
    def get_extra_info(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    drain: Generator ## = <generator>
    wait_closed: Generator ## = <generator>
    readexactly: Generator ## = <generator>
    aclose: Generator ## = <generator>
    awrite: Generator ## = <generator>
    awritestr: Generator ## = <generator>
    read: Generator ## = <generator>
    readinto: Generator ## = <generator>
    readline: Generator ## = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        ...


class Server():
    def close(self, *args, **kwargs) -> Incomplete:
        ...

    _serve: Generator ## = <generator>
    wait_closed: Generator ## = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        ...

open_connection: Generator ## = <generator>

class StreamWriter():
    def get_extra_info(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    drain: Generator ## = <generator>
    wait_closed: Generator ## = <generator>
    readexactly: Generator ## = <generator>
    aclose: Generator ## = <generator>
    awrite: Generator ## = <generator>
    awritestr: Generator ## = <generator>
    read: Generator ## = <generator>
    readinto: Generator ## = <generator>
    readline: Generator ## = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        ...

