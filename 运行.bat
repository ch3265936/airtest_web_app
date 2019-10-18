@echo off
del std.log
start cmd /K  "C:\Users\chihai\AppData\Local\Programs\Python\Python37\python.exe D:/airtest_runner-master/main.py>>std.log"