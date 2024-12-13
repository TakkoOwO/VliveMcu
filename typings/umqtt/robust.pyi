"""
Module: 'umqtt.robust' on micropython-v1.20.0-preview-esp32
"""
# MCU: {'family': 'micropython', 'version': '1.20.0-preview', 'build': '696', 'ver': '1.20.0-preview-696', 'port': 'esp32', 'board': '', 'cpu': 'ESP32S3', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Generator
from _typeshed import Incomplete


class MQTTClient():
    DEBUG: bool = False
    DELAY: int = 2
    def _send_str(self, *args, **kwargs) -> Incomplete:
        ...

    def set_last_will(self, *args, **kwargs) -> Incomplete:
        ...

    def ping(self, *args, **kwargs) -> Incomplete:
        ...

    def _recv_len(self, *args, **kwargs) -> Incomplete:
        ...

    def set_callback(self, *args, **kwargs) -> Incomplete:
        ...

    def delay(self, *args, **kwargs) -> Incomplete:
        ...

    def connect(self, *args, **kwargs) -> Incomplete:
        ...

    def log(self, *args, **kwargs) -> Incomplete:
        ...

    def subscribe(self, *args, **kwargs) -> Incomplete:
        ...

    def disconnect(self, *args, **kwargs) -> Incomplete:
        ...

    def wait_msg(self, *args, **kwargs) -> Incomplete:
        ...

    def reconnect(self, *args, **kwargs) -> Incomplete:
        ...

    def check_msg(self, *args, **kwargs) -> Incomplete:
        ...

    def publish(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

