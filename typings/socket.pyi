"""
Module: 'socket' on micropython-v1.20.0-preview-esp32
"""
# MCU: {'family': 'micropython', 'version': '1.20.0-preview', 'build': '696', 'ver': '1.20.0-preview-696', 'port': 'esp32', 'board': '', 'cpu': 'ESP32S3', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Generator
from _typeshed import Incomplete

AF_INET: int = 2
SOL_SOCKET: int = 4095
AF_INET6: int = 10
IPPROTO_TCP: int = 6
SOCK_STREAM: int = 1
IPPROTO_UDP: int = 17
SO_REUSEADDR: int = 4
SOCK_DGRAM: int = 2
SOCK_RAW: int = 3
IP_ADD_MEMBERSHIP: int = 3
IPPROTO_IP: int = 0
def getaddrinfo(*args, **kwargs) -> Incomplete:
    ...


class socket():
    def settimeout(self, *args, **kwargs) -> Incomplete:
        ...

    def accept(self, *args, **kwargs) -> Incomplete:
        ...

    def fileno(self, *args, **kwargs) -> Incomplete:
        ...

    def bind(self, *args, **kwargs) -> Incomplete:
        ...

    def connect(self, *args, **kwargs) -> Incomplete:
        ...

    def recvfrom(self, *args, **kwargs) -> Incomplete:
        ...

    def setsockopt(self, *args, **kwargs) -> Incomplete:
        ...

    def makefile(self, *args, **kwargs) -> Incomplete:
        ...

    def sendall(self, *args, **kwargs) -> Incomplete:
        ...

    def recv(self, *args, **kwargs) -> Incomplete:
        ...

    def readline(self, *args, **kwargs) -> Incomplete:
        ...

    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    def setblocking(self, *args, **kwargs) -> Incomplete:
        ...

    def send(self, *args, **kwargs) -> Incomplete:
        ...

    def listen(self, *args, **kwargs) -> Incomplete:
        ...

    def sendto(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

