import json
from venv.stats.process.pid_service import Pid_Service

class Pid_Stats_Serializer:

    def serialize_pid_stats(pid):
        return json.dumps(Pid_Service.get_pid_stats(pid).__dict__)