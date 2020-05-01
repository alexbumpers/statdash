from stats.process.ps import ps_output_to_json
# from stats.system.cpu.cpu_service import *
from stats.system.memory.mem_service import *
import psutil
import json

from models.process.Process import *

from venv.serializers.stats.cpu.cpu_serializer import Cpu_Serializer
from venv.serializers.stats.memory.memory_serializer import Memory_Serializer
from venv.serializers.stats.process.pid_stats_serializer import Pid_Stats_Serializer
from venv.stats.process.pid_service import Pid_Service


def main():
    # print(Memory_Serializer.serialize_memory())
    print(Pid_Service.get_pid_stats_all_pids())
    print(Cpu_Serializer.serialize_cpu())
    print(Pid_Stats_Serializer.serialize_pid_stats(2988))
if __name__ == "__main__":
    main()

