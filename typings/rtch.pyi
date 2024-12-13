"""
Module: 'rtch' on micropython-v1.20.0-preview-esp32
"""
# MCU: {'family': 'micropython', 'version': '1.20.0-preview', 'build': '696', 'ver': '1.20.0-preview-696', 'port': 'esp32', 'board': '', 'cpu': 'ESP32S3', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Generator
from _typeshed import Incomplete


class touch():
    def calibrate(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def activate(self, *args, **kwargs) -> Incomplete:
        ...

    read: Incomplete ## <class 'touch_read'> = <touch_read>
    def __init__(self, *argv, **kwargs) -> None:
        ...

