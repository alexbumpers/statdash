import json

from venv.models.system.cpu.cpu import CPU
from venv.stats.system.cpu.cpu_service import Cpu_Service


class Cpu_Serializer:

    @staticmethod
    def serialize_cpu():
        cpu = CPU(
            Cpu_Service.get_current_cpu()
        )
        return json.dumps(cpu.__dict__)