import psutil
import os




class Pid_Service:

    def get_mem_usage_by_pid(pid):
        process_id = psutil.Process(pid)
        return process_id.memory_percent()

    @staticmethod
    def get_all_memory_usage_for_all_pids():
        list_pids = psutil.pids()
        pid_to_memory_map = {}

        for p in list_pids:
            mem_percent = float("{:.2f}".format(psutil.Process(p).memory_percent()))
            pid_to_memory_map.update({p: mem_percent})

        return pid_to_memory_map