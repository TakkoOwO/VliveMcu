"""
Module: 'sys' on micropython-v1.20.0-preview-esp32
"""
# MCU: {'family': 'micropython', 'version': '1.20.0-preview', 'build': '696', 'ver': '1.20.0-preview-696', 'port': 'esp32', 'board': '', 'cpu': 'ESP32S3', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Generator
from _typeshed import Incomplete

ps1: str = '>>> '
byteorder: str = 'little'
ps2: str = '... '
version: str = '3.4.0; MicroPython v1.20.0-696-gfb095f2dd-dirty on 2024-12-03'
modules: dict = {}
argv: list = []
path: list = []
platform: str = 'esp32'
maxsize: int = 2147483647
version_info: tuple = ()
implementation: tuple = ()
def print_exception(*args, **kwargs) -> Incomplete:
    ...

def exit(*args, **kwargs) -> Incomplete:
    ...

stdin: Incomplete ## <class 'FileIO'> = <io.FileIO 0>
stdout: Incomplete ## <class 'FileIO'> = <io.FileIO 1>
stderr: Incomplete ## <class 'FileIO'> = <io.FileIO 2>
