"""
Module: '_thread' on micropython-v1.20.0-preview-esp32
"""
# MCU: {'family': 'micropython', 'version': '1.20.0-preview', 'build': '696', 'ver': '1.20.0-preview-696', 'port': 'esp32', 'board': '', 'cpu': 'ESP32S3', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Generator
from _typeshed import Incomplete

def get_ident(*args, **kwargs) -> Incomplete:
    ...

def allocate_lock(*args, **kwargs) -> Incomplete:
    ...

def exit(*args, **kwargs) -> Incomplete:
    ...

def stack_size(*args, **kwargs) -> Incomplete:
    ...

def start_new_thread(*args, **kwargs) -> Incomplete:
    ...


class LockType():
    def locked(self, *args, **kwargs) -> Incomplete:
        ...

    def acquire(self, *args, **kwargs) -> Incomplete:
        ...

    def release(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

