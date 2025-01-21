#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("localhost", 50051))
s.listen(16)

while True:
    fd, addr = s.accept()
    print("accepted:", addr)
    fd.close()
