import json

from venv.models.system.memory.memory import Memory
from venv.stats.system.memory.mem_service import Mem_Service


class Memory_Serializer:

    @staticmethod
    def serialize_memory():
        mem = Memory(
            Mem_Service.get_curr_mem(),
            Mem_Service.get_percent_of_memory_used(),
            Mem_Service.get_total_memory_in_gb()
        )
        return json.dumps(mem.__dict__)
