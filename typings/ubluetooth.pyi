"""
Module: 'ubluetooth' on micropython-v1.20.0-preview-esp32
"""
# MCU: {'family': 'micropython', 'version': '1.20.0-preview', 'build': '696', 'ver': '1.20.0-preview-696', 'port': 'esp32', 'board': '', 'cpu': 'ESP32S3', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Generator
from _typeshed import Incomplete

FLAG_READ: int = 2
FLAG_INDICATE: int = 32
FLAG_WRITE_NO_RESPONSE: int = 4
FLAG_WRITE: int = 8
FLAG_NOTIFY: int = 16

class BLE():
    def gattc_read(self, *args, **kwargs) -> Incomplete:
        ...

    def gap_scan(self, *args, **kwargs) -> Incomplete:
        ...

    def gattc_discover_services(self, *args, **kwargs) -> Incomplete:
        ...

    def config(self, *args, **kwargs) -> Incomplete:
        ...

    def gattc_write(self, *args, **kwargs) -> Incomplete:
        ...

    def active(self, *args, **kwargs) -> Incomplete:
        ...

    def gattc_discover_characteristics(self, *args, **kwargs) -> Incomplete:
        ...

    def gatts_read(self, *args, **kwargs) -> Incomplete:
        ...

    def gatts_indicate(self, *args, **kwargs) -> Incomplete:
        ...

    def gatts_write(self, *args, **kwargs) -> Incomplete:
        ...

    def gap_disconnect(self, *args, **kwargs) -> Incomplete:
        ...

    def gatts_notify(self, *args, **kwargs) -> Incomplete:
        ...

    def gattc_exchange_mtu(self, *args, **kwargs) -> Incomplete:
        ...

    def gattc_discover_descriptors(self, *args, **kwargs) -> Incomplete:
        ...

    def gap_connect(self, *args, **kwargs) -> Incomplete:
        ...

    def gap_pair(self, *args, **kwargs) -> Incomplete:
        ...

    def gap_passkey(self, *args, **kwargs) -> Incomplete:
        ...

    def gatts_set_buffer(self, *args, **kwargs) -> Incomplete:
        ...

    def gatts_register_services(self, *args, **kwargs) -> Incomplete:
        ...

    def gap_advertise(self, *args, **kwargs) -> Incomplete:
        ...

    def irq(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class UUID():
    def __init__(self, *argv, **kwargs) -> None:
        ...

