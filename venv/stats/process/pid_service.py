import psutil
import os

from venv.models.process.pid_stats import Pid_Stats


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

    @staticmethod
    def get_pid_stats(pid):
        # given a pid, get memory usage of that pid

        # given the same pid, get cpu usage

        # Construct a Pid_stats object such that is contains:
        # {
        #   "pid": "1234",
        #   "cpu_usage": "10.0",
        #   "mem_usage" : "54.0%"
        # }
        mem_percent = float("{:.2f}".format(psutil.Process(pid).memory_percent()))
        cpu_percent = float("{:.2f}".format(psutil.Process(pid).cpu_percent(1)))
        pid_stats = Pid_Stats(pid, mem_percent, cpu_percent)
        return pid_stats

    @staticmethod
    def get_pid_stats_all_pids():
        # Get all stats for all pids such that it returns a list of dictionaries as below:
        # [
        #   {
        #   "pid": "1234",
        #   "cpu_usage": "10.0",
        #   "mem_usage" : "54.0%"
        #   },
        #   {
        #   "pid": "4321",
        #   "cpu_usage": "5.0",
        #   "mem_usage" : "12.3%"
        #   },
        #   {
        #   "pid": "590",
        #   "cpu_usage": "42.0",
        #   "mem_usage" : "6.9%"
        #   }
        # ]

        list_of_pid_stat_objects = []
        all_pids = psutil.pids()
        for i in range(0, len(all_pids)):
            pid = all_pids[i]
            # print(pid)
            mem_percent = float("{:.2f}".format(psutil.Process(pid).memory_percent()))
            cpu_percent = float("{:.2f}".format(psutil.Process(pid).cpu_percent()))
            pid_stats = Pid_Stats(pid, mem_percent, cpu_percent)
            list_of_pid_stat_objects.append(pid_stats.__dict__)
        return list_of_pid_stat_objects