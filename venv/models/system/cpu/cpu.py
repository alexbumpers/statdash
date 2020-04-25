class CPU:
    current_cpu_utilization = 0.00
    # average_cpu_utilization_one_hour = 0

    # def __init__(self, current_cpu_utilization, average_cpu_utilization_one_hour):
    def __init__(self, current_cpu_utilization):
        self.current_cpu_utilization = current_cpu_utilization
        # self.average_cpu_utilization_one_hour = average_cpu_utilization_one_hour