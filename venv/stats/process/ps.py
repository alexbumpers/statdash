import subprocess
import json
from models.process.Process import Process

def ps_output_to_json(process):
    run_ps = subprocess.Popen(["ps", "-ef"], stdout=subprocess.PIPE)
    pipe_ps_to_grep = subprocess.Popen(["grep", process], stdin=run_ps.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    ps_pids = pipe_ps_to_grep.communicate()[0]
    ps_split = ps_pids.decode().split('\n')
    nfields = len(ps_split[0].split()) - 1
    ps_split = ps_split[1:]

    ps_array = []
    for row in ps_split:
        try:
            uid = row.split(None, nfields)[0]
            pid = row.split(None, nfields)[1]
            ppid = row.split(None, nfields)[2]
            c = row.split(None, nfields)[3]
            stime = row.split(None, nfields)[4]
            tty = row.split(None, nfields)[5]
            time = row.split(None, nfields)[6]
            cmd = row.split(None, nfields)[7]
            # Length of < 8 indicates no arguments for the command
            if (len(row.split(None, nfields)) > 8):
                args = row.split(None, nfields)[8]
            else:
                args = None
            # p = Process(uid, pid, ppid, c, stime, tty, time, cmd, args)
            # ps_array.append(json.dumps(p.__dict__))
            p = Process(uid, pid, ppid, c, stime, tty, time, cmd, args)
            ps_array.append(p.__dict__)

        except:
            print("ERROR")
    # print(ps_array)
    print(json.dumps(ps_array))
    run_ps.stdout.close()

# ADD OUTPUT FROM ABOVE TO JSON https://stackoverflow.com/questions/34489706/create-json-object-with-variables-from-an-array
####
# out, err = pipe_ps_to_grep.communicate()
# print('{0}'.format(out))
# print('{0}'.format(err))
# ps -ef headers
# uid, pid, ppid, c, stime, tty, time, cmd, args

# Currently prints "error" if there is no "args" field, create a way to check if there are any that lack args and then just continue the loop