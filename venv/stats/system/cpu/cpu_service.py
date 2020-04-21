import psutil

class Cpu_Service:
    @staticmethod
    def get_current_cpu():
        return psutil.cpu_percent(interval=.1)

    @staticmethod
    def get_cpu_average_over_n_hours(hours):
        n = hours
        return n

