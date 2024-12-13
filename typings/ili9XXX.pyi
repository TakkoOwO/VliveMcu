"""
Module: 'ili9XXX' on micropython-v1.20.0-preview-esp32
"""
# MCU: {'family': 'micropython', 'version': '1.20.0-preview', 'build': '696', 'ver': '1.20.0-preview-696', 'port': 'esp32', 'board': '', 'cpu': 'ESP32S3', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Generator
from _typeshed import Incomplete

REVERSE_LANDSCAPE: int = -4
COLOR_MODE_BGR: int = 8
PORTRAIT: int = -1
DISPLAY_TYPE_ILI9341: int = 1
DISPLAY_TYPE_ILI9488: int = 2
REVERSE_PORTRAIT: int = -3
COLOR_MODE_RGB: int = 0
MADCTL_MY: int = 128
MADCTL_ML: int = 16
DISPLAY_TYPE_ST7735: int = 5
MADCTL_MH: int = 4
MADCTL_MX: int = 64
MADCTL_MV: int = 32
DISPLAY_TYPE_ST7789: int = 4
ORIENTATION_TABLE: tuple = ()
LANDSCAPE: int = -2
DISPLAY_TYPE_GC9A01: int = 3

class ili9341():
    monitor_acc_time: int = 0
    monitor_count: int = 0
    cycles_in_ms: int = 160000
    monitor_acc_px: int = 0
    flush_acc_setup_cycles: int = 0
    init_cmds: list = []
    TRANS_BUFFER_LEN: int = 16
    flush_acc_dma_cycles: int = 0
    display_name: str = 'ili9XXX'
    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def send_trans_word(self, *args, **kwargs) -> Incomplete:
        ...

    def flush(self, *args, **kwargs) -> Incomplete:
        ...

    def power_down(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def madctl(self, *args, **kwargs) -> Incomplete:
        ...

    def monitor(self, *args, **kwargs) -> Incomplete:
        ...

    def send_data(self, *args, **kwargs) -> Incomplete:
        ...

    def spi_send_dma(self, *args, **kwargs) -> Incomplete:
        ...

    def stat(self, *args, **kwargs) -> Incomplete:
        ...

    def send_data_dma(self, *args, **kwargs) -> Incomplete:
        ...

    def disp_spi_init(self, *args, **kwargs) -> Incomplete:
        ...

    def send_cmd(self, *args, **kwargs) -> Incomplete:
        ...

    def spi_send(self, *args, **kwargs) -> Incomplete:
        ...

    start_time_ptr: Incomplete ## <class 'C_Pointer'> = struct C_Pointer
    init_async: Generator ## = <generator>
    trans_result_ptr: Incomplete ## <class 'C_Pointer'> = struct C_Pointer
    trans: Incomplete ## <class 'spi_transaction_t'> = struct spi_transaction_t
    end_time_ptr: Incomplete ## <class 'C_Pointer'> = struct C_Pointer
    _init: Generator ## = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ili9XXX():
    monitor_acc_time: int = 0
    monitor_count: int = 0
    cycles_in_ms: int = 160000
    monitor_acc_px: int = 0
    flush_acc_setup_cycles: int = 0
    init_cmds: list = []
    TRANS_BUFFER_LEN: int = 16
    flush_acc_dma_cycles: int = 0
    display_name: str = 'ili9XXX'
    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def send_trans_word(self, *args, **kwargs) -> Incomplete:
        ...

    def flush(self, *args, **kwargs) -> Incomplete:
        ...

    def power_down(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def madctl(self, *args, **kwargs) -> Incomplete:
        ...

    def monitor(self, *args, **kwargs) -> Incomplete:
        ...

    def send_data(self, *args, **kwargs) -> Incomplete:
        ...

    def spi_send_dma(self, *args, **kwargs) -> Incomplete:
        ...

    def stat(self, *args, **kwargs) -> Incomplete:
        ...

    def send_data_dma(self, *args, **kwargs) -> Incomplete:
        ...

    def disp_spi_init(self, *args, **kwargs) -> Incomplete:
        ...

    def send_cmd(self, *args, **kwargs) -> Incomplete:
        ...

    def spi_send(self, *args, **kwargs) -> Incomplete:
        ...

    start_time_ptr: Incomplete ## <class 'C_Pointer'> = struct C_Pointer
    init_async: Generator ## = <generator>
    trans_result_ptr: Incomplete ## <class 'C_Pointer'> = struct C_Pointer
    trans: Incomplete ## <class 'spi_transaction_t'> = struct spi_transaction_t
    end_time_ptr: Incomplete ## <class 'C_Pointer'> = struct C_Pointer
    _init: Generator ## = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        ...


class gc9a01():
    monitor_acc_time: int = 0
    monitor_count: int = 0
    cycles_in_ms: int = 160000
    monitor_acc_px: int = 0
    flush_acc_setup_cycles: int = 0
    init_cmds: list = []
    TRANS_BUFFER_LEN: int = 16
    flush_acc_dma_cycles: int = 0
    display_name: str = 'ili9XXX'
    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def send_trans_word(self, *args, **kwargs) -> Incomplete:
        ...

    def flush(self, *args, **kwargs) -> Incomplete:
        ...

    def power_down(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def madctl(self, *args, **kwargs) -> Incomplete:
        ...

    def monitor(self, *args, **kwargs) -> Incomplete:
        ...

    def send_data(self, *args, **kwargs) -> Incomplete:
        ...

    def spi_send_dma(self, *args, **kwargs) -> Incomplete:
        ...

    def stat(self, *args, **kwargs) -> Incomplete:
        ...

    def send_data_dma(self, *args, **kwargs) -> Incomplete:
        ...

    def disp_spi_init(self, *args, **kwargs) -> Incomplete:
        ...

    def send_cmd(self, *args, **kwargs) -> Incomplete:
        ...

    def spi_send(self, *args, **kwargs) -> Incomplete:
        ...

    start_time_ptr: Incomplete ## <class 'C_Pointer'> = struct C_Pointer
    init_async: Generator ## = <generator>
    trans_result_ptr: Incomplete ## <class 'C_Pointer'> = struct C_Pointer
    trans: Incomplete ## <class 'spi_transaction_t'> = struct spi_transaction_t
    end_time_ptr: Incomplete ## <class 'C_Pointer'> = struct C_Pointer
    _init: Generator ## = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        ...


class st7735():
    monitor_acc_time: int = 0
    monitor_count: int = 0
    cycles_in_ms: int = 160000
    monitor_acc_px: int = 0
    flush_acc_setup_cycles: int = 0
    init_cmds: list = []
    TRANS_BUFFER_LEN: int = 16
    flush_acc_dma_cycles: int = 0
    display_name: str = 'ili9XXX'
    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def send_trans_word(self, *args, **kwargs) -> Incomplete:
        ...

    def flush(self, *args, **kwargs) -> Incomplete:
        ...

    def power_down(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def madctl(self, *args, **kwargs) -> Incomplete:
        ...

    def monitor(self, *args, **kwargs) -> Incomplete:
        ...

    def send_data(self, *args, **kwargs) -> Incomplete:
        ...

    def spi_send_dma(self, *args, **kwargs) -> Incomplete:
        ...

    def stat(self, *args, **kwargs) -> Incomplete:
        ...

    def send_data_dma(self, *args, **kwargs) -> Incomplete:
        ...

    def disp_spi_init(self, *args, **kwargs) -> Incomplete:
        ...

    def send_cmd(self, *args, **kwargs) -> Incomplete:
        ...

    def spi_send(self, *args, **kwargs) -> Incomplete:
        ...

    start_time_ptr: Incomplete ## <class 'C_Pointer'> = struct C_Pointer
    init_async: Generator ## = <generator>
    trans_result_ptr: Incomplete ## <class 'C_Pointer'> = struct C_Pointer
    trans: Incomplete ## <class 'spi_transaction_t'> = struct spi_transaction_t
    end_time_ptr: Incomplete ## <class 'C_Pointer'> = struct C_Pointer
    _init: Generator ## = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ili9488():
    monitor_acc_time: int = 0
    monitor_count: int = 0
    cycles_in_ms: int = 160000
    monitor_acc_px: int = 0
    flush_acc_setup_cycles: int = 0
    init_cmds: list = []
    TRANS_BUFFER_LEN: int = 16
    flush_acc_dma_cycles: int = 0
    display_name: str = 'ili9XXX'
    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def send_trans_word(self, *args, **kwargs) -> Incomplete:
        ...

    def flush(self, *args, **kwargs) -> Incomplete:
        ...

    def power_down(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def madctl(self, *args, **kwargs) -> Incomplete:
        ...

    def monitor(self, *args, **kwargs) -> Incomplete:
        ...

    def send_data(self, *args, **kwargs) -> Incomplete:
        ...

    def spi_send_dma(self, *args, **kwargs) -> Incomplete:
        ...

    def stat(self, *args, **kwargs) -> Incomplete:
        ...

    def send_data_dma(self, *args, **kwargs) -> Incomplete:
        ...

    def disp_spi_init(self, *args, **kwargs) -> Incomplete:
        ...

    def send_cmd(self, *args, **kwargs) -> Incomplete:
        ...

    def spi_send(self, *args, **kwargs) -> Incomplete:
        ...

    start_time_ptr: Incomplete ## <class 'C_Pointer'> = struct C_Pointer
    init_async: Generator ## = <generator>
    trans_result_ptr: Incomplete ## <class 'C_Pointer'> = struct C_Pointer
    trans: Incomplete ## <class 'spi_transaction_t'> = struct spi_transaction_t
    end_time_ptr: Incomplete ## <class 'C_Pointer'> = struct C_Pointer
    _init: Generator ## = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        ...


class st7789():
    monitor_acc_time: int = 0
    monitor_count: int = 0
    cycles_in_ms: int = 160000
    monitor_acc_px: int = 0
    flush_acc_setup_cycles: int = 0
    init_cmds: list = []
    TRANS_BUFFER_LEN: int = 16
    flush_acc_dma_cycles: int = 0
    display_name: str = 'ili9XXX'
    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def send_trans_word(self, *args, **kwargs) -> Incomplete:
        ...

    def flush(self, *args, **kwargs) -> Incomplete:
        ...

    def power_down(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def madctl(self, *args, **kwargs) -> Incomplete:
        ...

    def monitor(self, *args, **kwargs) -> Incomplete:
        ...

    def send_data(self, *args, **kwargs) -> Incomplete:
        ...

    def spi_send_dma(self, *args, **kwargs) -> Incomplete:
        ...

    def stat(self, *args, **kwargs) -> Incomplete:
        ...

    def send_data_dma(self, *args, **kwargs) -> Incomplete:
        ...

    def disp_spi_init(self, *args, **kwargs) -> Incomplete:
        ...

    def send_cmd(self, *args, **kwargs) -> Incomplete:
        ...

    def spi_send(self, *args, **kwargs) -> Incomplete:
        ...

    start_time_ptr: Incomplete ## <class 'C_Pointer'> = struct C_Pointer
    init_async: Generator ## = <generator>
    trans_result_ptr: Incomplete ## <class 'C_Pointer'> = struct C_Pointer
    trans: Incomplete ## <class 'spi_transaction_t'> = struct spi_transaction_t
    end_time_ptr: Incomplete ## <class 'C_Pointer'> = struct C_Pointer
    _init: Generator ## = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        ...


class ili9488g():
    monitor_acc_time: int = 0
    monitor_count: int = 0
    cycles_in_ms: int = 160000
    monitor_acc_px: int = 0
    flush_acc_setup_cycles: int = 0
    init_cmds: list = []
    TRANS_BUFFER_LEN: int = 16
    flush_acc_dma_cycles: int = 0
    display_name: str = 'ili9XXX'
    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def send_trans_word(self, *args, **kwargs) -> Incomplete:
        ...

    def flush(self, *args, **kwargs) -> Incomplete:
        ...

    def power_down(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def madctl(self, *args, **kwargs) -> Incomplete:
        ...

    def monitor(self, *args, **kwargs) -> Incomplete:
        ...

    def send_data(self, *args, **kwargs) -> Incomplete:
        ...

    def spi_send_dma(self, *args, **kwargs) -> Incomplete:
        ...

    def stat(self, *args, **kwargs) -> Incomplete:
        ...

    def send_data_dma(self, *args, **kwargs) -> Incomplete:
        ...

    def disp_spi_init(self, *args, **kwargs) -> Incomplete:
        ...

    def send_cmd(self, *args, **kwargs) -> Incomplete:
        ...

    def spi_send(self, *args, **kwargs) -> Incomplete:
        ...

    start_time_ptr: Incomplete ## <class 'C_Pointer'> = struct C_Pointer
    init_async: Generator ## = <generator>
    trans_result_ptr: Incomplete ## <class 'C_Pointer'> = struct C_Pointer
    trans: Incomplete ## <class 'spi_transaction_t'> = struct spi_transaction_t
    end_time_ptr: Incomplete ## <class 'C_Pointer'> = struct C_Pointer
    _init: Generator ## = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        ...

