"""
Module: 'urequests' on micropython-v1.20.0-preview-esp32
"""
# MCU: {'family': 'micropython', 'version': '1.20.0-preview', 'build': '696', 'ver': '1.20.0-preview-696', 'port': 'esp32', 'board': '', 'cpu': 'ESP32S3', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Generator
from _typeshed import Incomplete

def post(*args, **kwargs) -> Incomplete:
    ...

def delete(*args, **kwargs) -> Incomplete:
    ...

def patch(*args, **kwargs) -> Incomplete:
    ...

def request(*args, **kwargs) -> Incomplete:
    ...

def put(*args, **kwargs) -> Incomplete:
    ...

def get(*args, **kwargs) -> Incomplete:
    ...

def head(*args, **kwargs) -> Incomplete:
    ...


class Response():
    def json(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    content: Incomplete ## <class 'property'> = <property>
    text: Incomplete ## <class 'property'> = <property>
    def __init__(self, *argv, **kwargs) -> None:
        ...

