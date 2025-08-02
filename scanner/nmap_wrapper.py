import subprocess
import json

def run_nmap_scan(target):
    command = ["nmap", "-sV", "-oX", "-", target]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        raise Exception("Nmap scan failed: " + result.stderr)

    return result.stdout  # XML çıxış
