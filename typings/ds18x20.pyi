"""
Module: 'ds18x20' on micropython-v1.20.0-preview-esp32
"""
# MCU: {'family': 'micropython', 'version': '1.20.0-preview', 'build': '696', 'ver': '1.20.0-preview-696', 'port': 'esp32', 'board': '', 'cpu': 'ESP32S3', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Generator
from _typeshed import Incomplete

def const(*args, **kwargs) -> Incomplete:
    ...


class DS18X20():
    def read_temp(self, *args, **kwargs) -> Incomplete:
        ...

    def convert_temp(self, *args, **kwargs) -> Incomplete:
        ...

    def read_scratch(self, *args, **kwargs) -> Incomplete:
        ...

    def write_scratch(self, *args, **kwargs) -> Incomplete:
        ...

    def scan(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

