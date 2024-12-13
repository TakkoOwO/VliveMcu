"""
Module: 'machine' on micropython-v1.20.0-preview-esp32
"""
# MCU: {'family': 'micropython', 'version': '1.20.0-preview', 'build': '696', 'ver': '1.20.0-preview-696', 'port': 'esp32', 'board': '', 'cpu': 'ESP32S3', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Generator
from _typeshed import Incomplete

PWRON_RESET: int = 1
SOFT_RESET: int = 5
HARD_RESET: int = 2
WDT_RESET: int = 3
TOUCHPAD_WAKE: int = 5
SLEEP: int = 2
PIN_WAKE: int = 2
EXT0_WAKE: int = 2
ULP_WAKE: int = 6
DEEPSLEEP: int = 4
EXT1_WAKE: int = 3
DEEPSLEEP_RESET: int = 4
TIMER_WAKE: int = 4
def soft_reset(*args, **kwargs) -> Incomplete:
    ...

def dht_readinto(*args, **kwargs) -> Incomplete:
    ...

def reset(*args, **kwargs) -> Incomplete:
    ...

def idle(*args, **kwargs) -> Incomplete:
    ...

def lightsleep(*args, **kwargs) -> Incomplete:
    ...

def unique_id(*args, **kwargs) -> Incomplete:
    ...

def deepsleep(*args, **kwargs) -> Incomplete:
    ...

def wake_reason(*args, **kwargs) -> Incomplete:
    ...

def sleep(*args, **kwargs) -> Incomplete:
    ...

def reset_cause(*args, **kwargs) -> Incomplete:
    ...

def enable_irq(*args, **kwargs) -> Incomplete:
    ...

def bitstream(*args, **kwargs) -> Incomplete:
    ...

def time_pulse_us(*args, **kwargs) -> Incomplete:
    ...

def disable_irq(*args, **kwargs) -> Incomplete:
    ...

def freq(*args, **kwargs) -> Incomplete:
    ...


class SPI():
    LSB: int = 1
    MSB: int = 0
    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def write_readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class I2C():
    def scan(self, *args, **kwargs) -> Incomplete:
        ...

    def readfrom_mem(self, *args, **kwargs) -> Incomplete:
        ...

    def writevto(self, *args, **kwargs) -> Incomplete:
        ...

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def readfrom_mem_into(self, *args, **kwargs) -> Incomplete:
        ...

    def readfrom(self, *args, **kwargs) -> Incomplete:
        ...

    def writeto_mem(self, *args, **kwargs) -> Incomplete:
        ...

    def start(self, *args, **kwargs) -> Incomplete:
        ...

    def readfrom_into(self, *args, **kwargs) -> Incomplete:
        ...

    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def writeto(self, *args, **kwargs) -> Incomplete:
        ...

    def stop(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class I2S():
    TX: int = 5
    MONO: int = 0
    RX: int = 9
    STEREO: int = 1
    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def shift(self, *args, **kwargs) -> Incomplete:
        ...

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def irq(self, *args, **kwargs) -> Incomplete:
        ...

    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class PWM():
    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def duty_u16(self, *args, **kwargs) -> Incomplete:
        ...

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def duty_ns(self, *args, **kwargs) -> Incomplete:
        ...

    def freq(self, *args, **kwargs) -> Incomplete:
        ...

    def duty(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class RTC():
    def memory(self, *args, **kwargs) -> Incomplete:
        ...

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def datetime(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class WDT():
    def feed(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Signal():
    def off(self, *args, **kwargs) -> Incomplete:
        ...

    def on(self, *args, **kwargs) -> Incomplete:
        ...

    def value(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class SoftI2C():
    def scan(self, *args, **kwargs) -> Incomplete:
        ...

    def readfrom_mem(self, *args, **kwargs) -> Incomplete:
        ...

    def writevto(self, *args, **kwargs) -> Incomplete:
        ...

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def readfrom_mem_into(self, *args, **kwargs) -> Incomplete:
        ...

    def readfrom(self, *args, **kwargs) -> Incomplete:
        ...

    def writeto_mem(self, *args, **kwargs) -> Incomplete:
        ...

    def start(self, *args, **kwargs) -> Incomplete:
        ...

    def readfrom_into(self, *args, **kwargs) -> Incomplete:
        ...

    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def writeto(self, *args, **kwargs) -> Incomplete:
        ...

    def stop(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class SoftSPI():
    LSB: int = 1
    MSB: int = 0
    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def write_readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class TouchPad():
    def config(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Timer():
    PERIODIC: int = 1
    ONE_SHOT: int = 0
    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def value(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class ADC():
    ATTN_0DB: int = 0
    ATTN_2_5DB: int = 1
    WIDTH_12BIT: int = 12
    ATTN_6DB: int = 2
    ATTN_11DB: int = 3
    def read_u16(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def atten(self, *args, **kwargs) -> Incomplete:
        ...

    def block(self, *args, **kwargs) -> Incomplete:
        ...

    def read_uv(self, *args, **kwargs) -> Incomplete:
        ...

    def width(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class SDCard():
    def info(self, *args, **kwargs) -> Incomplete:
        ...

    def ioctl(self, *args, **kwargs) -> Incomplete:
        ...

    def writeblocks(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def readblocks(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class ADCBlock():
    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def connect(self, *args, **kwargs) -> Incomplete:
        ...

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


class UART():
    INV_CTS: int = 8
    RTS: int = 1
    INV_RTS: int = 64
    INV_TX: int = 32
    CTS: int = 2
    INV_RX: int = 4
    def txdone(self, *args, **kwargs) -> Incomplete:
        ...

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def flush(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def any(self, *args, **kwargs) -> Incomplete:
        ...

    def deinit(self, *args, **kwargs) -> Incomplete:
        ...

    def sendbreak(self, *args, **kwargs) -> Incomplete:
        ...

    def readline(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

mem32: Incomplete ## <class 'mem'> = <32-bit memory>
mem16: Incomplete ## <class 'mem'> = <16-bit memory>
mem8: Incomplete ## <class 'mem'> = <8-bit memory>
