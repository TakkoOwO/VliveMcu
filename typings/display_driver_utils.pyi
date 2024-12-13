"""
Module: 'display_driver_utils' on micropython-v1.20.0-preview-esp32
"""
# MCU: {'family': 'micropython', 'version': '1.20.0-preview', 'build': '696', 'ver': '1.20.0-preview-696', 'port': 'esp32', 'board': '', 'cpu': 'ESP32S3', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Generator
from _typeshed import Incomplete

lv_utils_available: bool = True
ORIENT_LANDSCAPE: bool = False
ORIENT_PORTRAIT: bool = True

class driver():
    def init_gui_ili9341(self, *args, **kwargs) -> Incomplete:
        ...

    def init_gui_twatch(self, *args, **kwargs) -> Incomplete:
        ...

    def init_gui(self, *args, **kwargs) -> Incomplete:
        ...

    def init_gui_SDL(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

