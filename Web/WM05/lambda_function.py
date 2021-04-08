import json
import subprocess
# Config
cmd = "ls -l "
def filtering(cmd, params):
    # Filter spaces and || and ;
    filter = [" ", "||", ";"]
    for f in filter:
        if f in params:
            return "filtered"
    output = cmd + params
    return output

def command(params):
    params = ''.join(params)
    combined = filtering(cmd, params)
    if combined == "filtered":
        return "Error: Invalid Character Detected."
    print(combined)
    out = subprocess.run(combined, shell=True, stdout=subprocess.PIPE)
    out = out.stdout.decode()
    out = out.splitlines()
    for item in out:
        out.remove(item)
    out = "".join(out)
    return out.replace("&lt;", "&lt;").replace("&gt;", "&gt;")
