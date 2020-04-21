class Memory:

    current_memory = 0.00
    total_system_memory = 0.00
    percent_memory_used = 0.00

    def __init__(self, curr_memory, percent_mem_used, total_memory):
        self.current_memory = curr_memory
        self.total_system_memory = total_memory
        self.percent_memory_used = percent_mem_used