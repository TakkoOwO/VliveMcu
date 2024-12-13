"""
Module: 'xpt2046' on micropython-v1.20.0-preview-esp32
"""
# MCU: {'family': 'micropython', 'version': '1.20.0-preview', 'build': '696', 'ver': '1.20.0-preview-696', 'port': 'esp32', 'board': '', 'cpu': 'ESP32S3', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Generator
from _typeshed import Incomplete


class xpt2046():
    cycles_in_ms: int = 160000
    CMD_X_READ: int = 288
    CMD_Z1_READ: int = 352
    CMD_Z2_READ: int = 384
    CMD_Y_READ: int = 416
    MAX_RAW_COORD: int = 4095
    def spi_init(self, *args, **kwargs) -> Incomplete:
        ...

    def xpt_cmds(self, *args, **kwargs) -> Incomplete:
        ...

    def get_pressure(self, *args, **kwargs) -> Incomplete:
        ...

    def get_med_coords(self, *args, **kwargs) -> Incomplete:
        ...

    def stat(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    def get_coords(self, *args, **kwargs) -> Incomplete:
        ...

    def calibrate(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    end_time_ptr: Incomplete ## <class 'C_Pointer'> = struct C_Pointer
    start_time_ptr: Incomplete ## <class 'C_Pointer'> = struct C_Pointer
    trans_result_ptr: Incomplete ## <class 'C_Pointer'> = struct C_Pointer
    def __init__(self, *argv, **kwargs) -> None:
        ...


class Pin():
    DRIVE_2: int = 2
    IRQ_RISING: int = 1
    OUT: int = 3
    IRQ_FALLING: int = 2
    PULL_DOWN: int = 1
    DRIVE_3: int = 3
    WAKE_HIGH: int = 5
    DRIVE_1: int = 1
    DRIVE_0: int = 0
    PULL_UP: int = 2
    WAKE_LOW: int = 4
    OPEN_DRAIN: int = 7
    IN: int = 1
    def value(self, *args, **kwargs) -> Incomplete:
        ...

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def on(self, *args, **kwargs) -> Incomplete:
        ...

    def irq(self, *args, **kwargs) -> Incomplete:
        ...

    def off(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

