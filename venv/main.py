from stats.process.ps import ps_output_to_json
# from stats.system.cpu.cpu_service import *
from stats.system.memory.mem_service import *
import json

from models.process.Process import *

from venv.serializers.stats.memory.memory_serializer import Memory_Serializer


def main():
    # ps_output_to_json("spotify")
    # p = Process("uid", "pid", "ppid", "c", "stime", "tty", "time", "cmd", "args")
    # print(json.dumps(p.__dict__))
    print(Memory_Serializer.serialize_memory())

if __name__ == "__main__":
    main()

