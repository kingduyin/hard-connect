#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：test.py
@Author  ：KING
@Date    ：2024/6/13 12:51 
"""
import time
from functools import wraps
from hard_connect.hard_conn import hard_conn as HardConnect


def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer


@coroutine
def receive_generator():
    while True:
        data = yield

        print('Data:', data)


def test_conn():
    import logging
    recv_gen = receive_generator()
    # hard = HardConnect(conn_type='socket', ip='127.0.0.1', port=60000, logging_level=logging.INFO)
    # hard.start()
    hard = HardConnect(conn_type='socket', ip='192.168.0.100', port=5000, logging_level=logging.INFO)
    hard1 = HardConnect(
        conn_type='socket', ip='192.168.0.100', port=5001,  receive_generator=recv_gen
    )
    # hard = HardConnect(conn_type='serial', device='/dev/tty.usbmodem1202', baud_rate=115200)
    hard1.start()
    hard.send_receive('>vcm upload(on)')
    print('----', hard.send_receive('>vcm force(10)'))
    time.sleep(1)
    print('----', hard.send_receive('>vcm force(10)'))
    # print(hard.send_receive('>vcm force(10)'))
    # hard.send('>vcm force(50)')
    # hard.send_receive('>vcm force(100)')
    # hard.send('>vcm force(0)')
    print(hard)


if __name__ == '__main__':
    test_conn()