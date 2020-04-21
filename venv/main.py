from stats.process.ps import ps_output_to_json
from stats.system.cpu.cpu_service import *
import json

from models.process.Process import Process

def main():
    # ps_output_to_json("spotify")
    # p = Process("uid", "pid", "ppid", "c", "stime", "tty", "time", "cmd", "args")
    # print(json.dumps(p.__dict__))
    Cpu_Service.get_current_cpu()

if __name__ == "__main__":
    main()

