"""
Module: 'framebuf' on micropython-v1.20.0-preview-esp32
"""
# MCU: {'family': 'micropython', 'version': '1.20.0-preview', 'build': '696', 'ver': '1.20.0-preview-696', 'port': 'esp32', 'board': '', 'cpu': 'ESP32S3', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Generator
from _typeshed import Incomplete

MONO_VLSB: int = 0
GS8: int = 6
GS2_HMSB: int = 5
RGB565: int = 1
GS4_HMSB: int = 2
MONO_HLSB: int = 3
MVLSB: int = 0
MONO_HMSB: int = 4
def FrameBuffer1(*args, **kwargs) -> Incomplete:
    ...


class FrameBuffer():
    def ellipse(self, *args, **kwargs) -> Incomplete:
        ...

    def rect(self, *args, **kwargs) -> Incomplete:
        ...

    def poly(self, *args, **kwargs) -> Incomplete:
        ...

    def vline(self, *args, **kwargs) -> Incomplete:
        ...

    def fill_rect(self, *args, **kwargs) -> Incomplete:
        ...

    def pixel(self, *args, **kwargs) -> Incomplete:
        ...

    def fill(self, *args, **kwargs) -> Incomplete:
        ...

    def text(self, *args, **kwargs) -> Incomplete:
        ...

    def line(self, *args, **kwargs) -> Incomplete:
        ...

    def scroll(self, *args, **kwargs) -> Incomplete:
        ...

    def hline(self, *args, **kwargs) -> Incomplete:
        ...

    def blit(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

