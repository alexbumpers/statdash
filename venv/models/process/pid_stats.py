class Pid_Stats:
    pid = ''
    memory_usage = None
    cpu_usage = None

    def __init__(self, pid, memory_usage, cpu_usage):
        self.pid = pid
        self.memory_usage = memory_usage
        self.cpu_usage = cpu_usage
