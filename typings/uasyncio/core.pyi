"""
Module: 'uasyncio.core' on micropython-v1.20.0-preview-esp32
"""
# MCU: {'family': 'micropython', 'version': '1.20.0-preview', 'build': '696', 'ver': '1.20.0-preview-696', 'port': 'esp32', 'board': '', 'cpu': 'ESP32S3', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Generator
from _typeshed import Incomplete

_exc_context: dict = {}
def ticks_diff(*args, **kwargs) -> Incomplete:
    ...

def ticks(*args, **kwargs) -> Incomplete:
    ...

def create_task(*args, **kwargs) -> Incomplete:
    ...

def sleep(*args, **kwargs) -> Incomplete:
    ...

def current_task(*args, **kwargs) -> Incomplete:
    ...

def new_event_loop(*args, **kwargs) -> Incomplete:
    ...

def get_event_loop(*args, **kwargs) -> Incomplete:
    ...

def run(*args, **kwargs) -> Incomplete:
    ...

def ticks_add(*args, **kwargs) -> Incomplete:
    ...

def run_until_complete(*args, **kwargs) -> Incomplete:
    ...

def _promote_to_task(*args, **kwargs) -> Incomplete:
    ...

def sleep_ms(*args, **kwargs) -> Incomplete:
    ...


class TimeoutError(Exception):
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

_io_queue: Incomplete ## <class 'IOQueue'> = <IOQueue object at ...>

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


class Task():
    def __init__(self, *argv, **kwargs) -> None:
        ...

_stopper: Generator ## = <generator>

class CancelledError(Exception):
    ...

class SingletonGenerator():
    def __init__(self, *argv, **kwargs) -> None:
        ...

_stop_task: Incomplete ## <class 'NoneType'> = None
_task_queue: Incomplete ## <class 'TaskQueue'> = <TaskQueue>
