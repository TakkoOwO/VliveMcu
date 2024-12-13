"""
Module: 'uftpd' on micropython-v1.20.0-preview-esp32
"""
# MCU: {'family': 'micropython', 'version': '1.20.0-preview', 'build': '696', 'ver': '1.20.0-preview-696', 'port': 'esp32', 'board': '', 'cpu': 'ESP32S3', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Generator
from _typeshed import Incomplete

client_list: list = []
client_busy: bool = False
verbose_l: int = 0
_month_name: tuple = ()
ftpsockets: list = []
def alloc_emergency_exception_buf(*args, **kwargs) -> Incomplete:
    ...

def num_ip(*args, **kwargs) -> Incomplete:
    ...

def log_msg(*args, **kwargs) -> Incomplete:
    ...

def localtime(*args, **kwargs) -> Incomplete:
    ...

def start(*args, **kwargs) -> Incomplete:
    ...

def stop(*args, **kwargs) -> Incomplete:
    ...

def close_client(*args, **kwargs) -> Incomplete:
    ...

def restart(*args, **kwargs) -> Incomplete:
    ...

def accept_ftp_connect(*args, **kwargs) -> Incomplete:
    ...

def sleep_ms(*args, **kwargs) -> Incomplete:
    ...


class FTP_client():
    def split_path(self, *args, **kwargs) -> Incomplete:
        ...

    def exec_ftp_command(self, *args, **kwargs) -> Incomplete:
        ...

    def make_description(self, *args, **kwargs) -> Incomplete:
        ...

    def send_list_data(self, *args, **kwargs) -> Incomplete:
        ...

    def save_file_data(self, *args, **kwargs) -> Incomplete:
        ...

    def open_dataclient(self, *args, **kwargs) -> Incomplete:
        ...

    def send_file_data(self, *args, **kwargs) -> Incomplete:
        ...

    def get_absolute_path(self, *args, **kwargs) -> Incomplete:
        ...

    def fncmp(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

datasocket: Incomplete ## <class 'socket'> = <socket>
