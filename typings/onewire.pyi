"""
Module: 'onewire' on micropython-v1.20.0-preview-esp32
"""
# MCU: {'family': 'micropython', 'version': '1.20.0-preview', 'build': '696', 'ver': '1.20.0-preview-696', 'port': 'esp32', 'board': '', 'cpu': 'ESP32S3', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Generator
from _typeshed import Incomplete


class OneWireError(Exception):
    ...

class OneWire():
    MATCH_ROM: int = 85
    SKIP_ROM: int = 204
    SEARCH_ROM: int = 240
    def _search_rom(self, *args, **kwargs) -> Incomplete:
        ...

    def readbyte(self, *args, **kwargs) -> Incomplete:
        ...

    def reset(self, *args, **kwargs) -> Incomplete:
        ...

    def select_rom(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def writebyte(self, *args, **kwargs) -> Incomplete:
        ...

    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def crc8(self, *args, **kwargs) -> Incomplete:
        ...

    def writebit(self, *args, **kwargs) -> Incomplete:
        ...

    def readbit(self, *args, **kwargs) -> Incomplete:
        ...

    def scan(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

