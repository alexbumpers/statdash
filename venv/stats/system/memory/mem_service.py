import psutil

class Mem_Service:
    @staticmethod
    def get_curr_mem():
        curr_mem_used_in_gb = float("{:.2f}".format(psutil.virtual_memory().used / 1000000000))
        return curr_mem_used_in_gb

    @staticmethod
    def get_total_memory_in_gb():
        total_mem_to_gb_val = float("{:.2f}".format(psutil.virtual_memory().total / 1000000000))
        return total_mem_to_gb_val

    @staticmethod
    def get_percent_of_memory_used():
        return psutil.virtual_memory().percent

    @staticmethod
    def get_available_memory_remaining():
        available_mem_to_gb_val = float("{:.2f}".format(psutil.virtual_memory().available / 1000000000))
        return available_mem_to_gb_val