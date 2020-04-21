from json import JSONEncoder
import json


class Process:
    uid = ""
    pid = ""
    ppid = ""
    c = ""
    stime = ""
    tty = ""
    time = ""
    cmd = ""
    # Length of < 8 indicates no arguments for the command
    args = ""

    def __init__(self, uid, pid, ppid, c, stime, tty, time, cmd, args):
        self.uid = uid
        self.pid = pid
        self.ppid = ppid
        self.c = c
        self.stime = stime
        self.tty = tty
        self.time = time
        self.cmd = cmd
        self.args = args

    class ClassEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__