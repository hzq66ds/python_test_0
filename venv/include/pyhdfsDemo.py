#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pyhdfs


def gethdfsclient(str):
    print(str)

client = pyhdfs.HdfsClient(hosts="172.16.1.240,9000", user_name="root")

testPath = "/user/root/test"
if client.exists(testPath):
    print(testPath, "is exist")
    gethdfsclient ("111111")
else:
    print(client.mkdirs(testPath))

