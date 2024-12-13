"""
Module: 'utelnetserver' on micropython-v1.20.0-preview-esp32
"""
# MCU: {'family': 'micropython', 'version': '1.20.0-preview', 'build': '696', 'ver': '1.20.0-preview-696', 'port': 'esp32', 'board': '', 'cpu': 'ESP32S3', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Generator
from _typeshed import Incomplete

def stop(*args, **kwargs) -> Incomplete:
    ...

def accept_telnet_connect(*args, **kwargs) -> Incomplete:
    ...

def start(*args, **kwargs) -> Incomplete:
    ...


class TelnetWrapper():
    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

last_client_socket: Incomplete ## <class 'NoneType'> = None
server_socket: Incomplete ## <class 'NoneType'> = None

class IOBase():
    def __init__(self, *argv, **kwargs) -> None:
        ...

