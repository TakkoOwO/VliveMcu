"""
Module: 'uasyncio.__init__' on micropython-v1.20.0-preview-esp32
"""
# MCU: {'family': 'micropython', 'version': '1.20.0-preview', 'build': '696', 'ver': '1.20.0-preview-696', 'port': 'esp32', 'board': '', 'cpu': 'ESP32S3', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Generator
from _typeshed import Incomplete

_attrs: dict = {}
def run(*args, **kwargs) -> Incomplete:
    ...

def ticks_diff(*args, **kwargs) -> Incomplete:
    ...

def ticks_add(*args, **kwargs) -> Incomplete:
    ...

def current_task(*args, **kwargs) -> Incomplete:
    ...

def ticks(*args, **kwargs) -> Incomplete:
    ...

def new_event_loop(*args, **kwargs) -> Incomplete:
    ...

def wait_for_ms(*args, **kwargs) -> Incomplete:
    ...

def run_until_complete(*args, **kwargs) -> Incomplete:
    ...

def sleep(*args, **kwargs) -> Incomplete:
    ...

def create_task(*args, **kwargs) -> Incomplete:
    ...

def get_event_loop(*args, **kwargs) -> Incomplete:
    ...

def sleep_ms(*args, **kwargs) -> Incomplete:
    ...


class IOQueue():
    def _enqueue(self, *args, **kwargs) -> Incomplete:
        ...

    def queue_read(self, *args, **kwargs) -> Incomplete:
        ...

    def _dequeue(self, *args, **kwargs) -> Incomplete:
        ...

    def remove(self, *args, **kwargs) -> Incomplete:
        ...

    def queue_write(self, *args, **kwargs) -> Incomplete:
        ...

    def wait_io_event(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

start_server: Generator ## = <generator>

class Lock():
    def locked(self, *args, **kwargs) -> Incomplete:
        ...

    def release(self, *args, **kwargs) -> Incomplete:
        ...

    acquire: Generator ## = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        ...


class Event():
    def set(self, *args, **kwargs) -> Incomplete:
        ...

    def is_set(self, *args, **kwargs) -> Incomplete:
        ...

    def clear(self, *args, **kwargs) -> Incomplete:
        ...

    wait: Generator ## = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        ...


class Loop():
    def create_task(self, *args, **kwargs) -> Incomplete:
        ...

    def run_forever(self, *args, **kwargs) -> Incomplete:
        ...

    def run_until_complete(self, *args, **kwargs) -> Incomplete:
        ...

    def default_exception_handler(self, *args, **kwargs) -> Incomplete:
        ...

    def get_exception_handler(self, *args, **kwargs) -> Incomplete:
        ...

    def call_exception_handler(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    def stop(self, *args, **kwargs) -> Incomplete:
        ...

    def set_exception_handler(self, *args, **kwargs) -> Incomplete:
        ...

    _exc_handler: Incomplete ## <class 'NoneType'> = None
    def __init__(self, *argv, **kwargs) -> None:
        ...


class StreamWriter():
    def get_extra_info(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    drain: Generator ## = <generator>
    wait_closed: Generator ## = <generator>
    readexactly: Generator ## = <generator>
    aclose: Generator ## = <generator>
    awrite: Generator ## = <generator>
    awritestr: Generator ## = <generator>
    read: Generator ## = <generator>
    readinto: Generator ## = <generator>
    readline: Generator ## = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        ...

wait_for: Generator ## = <generator>

class StreamReader():
    def get_extra_info(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    drain: Generator ## = <generator>
    wait_closed: Generator ## = <generator>
    readexactly: Generator ## = <generator>
    aclose: Generator ## = <generator>
    awrite: Generator ## = <generator>
    awritestr: Generator ## = <generator>
    read: Generator ## = <generator>
    readinto: Generator ## = <generator>
    readline: Generator ## = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        ...


class TaskQueue():
    def peek(self, *args, **kwargs) -> Incomplete:
        ...

    def push(self, *args, **kwargs) -> Incomplete:
        ...

    def remove(self, *args, **kwargs) -> Incomplete:
        ...

    def pop(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

open_connection: Generator ## = <generator>

class Task():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class SingletonGenerator():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class TimeoutError(Exception):
    ...

class CancelledError(Exception):
    ...

class ThreadSafeFlag():
    def set(self, *args, **kwargs) -> Incomplete:
        ...

    def ioctl(self, *args, **kwargs) -> Incomplete:
        ...

    def clear(self, *args, **kwargs) -> Incomplete:
        ...

    wait: Generator ## = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        ...

gather: Generator ## = <generator>
