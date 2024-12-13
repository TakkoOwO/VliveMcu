"""
Module: 'lv_utils' on micropython-v1.20.0-preview-esp32
"""
# MCU: {'family': 'micropython', 'version': '1.20.0-preview', 'build': '696', 'ver': '1.20.0-preview-696', 'port': 'esp32', 'board': '', 'cpu': 'ESP32S3', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Generator
from _typeshed import Incomplete

default_timer_id: int = 0
uasyncio_available: bool = True

class event_loop():
    def is_running(self, *args, **kwargs) -> Incomplete:
        ...

    def enable(self, *args, **kwargs) -> Incomplete:
        ...

    def current_instance(self, *args, **kwargs) -> Incomplete:
        ...

    def default_exception_sink(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def task_handler(self, *args, **kwargs) -> Incomplete:
        ...

    def timer_cb(self, *args, **kwargs) -> Incomplete:
        ...

    def disable(self, *args, **kwargs) -> Incomplete:
        ...

    _current_instance: Incomplete ## <class 'NoneType'> = None
    async_timer: Generator ## = <generator>
    async_refresh: Generator ## = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        ...


class Timer():
    PERIODIC: int = 1
    ONE_SHOT: int = 0
    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def value(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

