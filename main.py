import os
import subprocess
import psutil


context = {}


def os_information():
    context['host_name'] = subprocess.check_output("hostname -I", shell=True).strip().decode()
    context['linux'] = subprocess.check_output("uname -v", shell=True).strip().decode().split('~')[1]
    context['uptime'] = subprocess.check_output("uptime", shell=True).strip().decode()
    context['kernel'] = subprocess.check_output("uname -r", shell=True).strip().decode()
    context['bash_version'] = subprocess.check_output("bash --version", shell=True).strip().decode()
    return 0


def cpu():
    context['cpu_avg'] = os.getloadavg()
    context['cpu_information'] = subprocess.check_output("lscpu", shell=True).strip().decode()
    return 0


def memory_information():
    context['memory'] = subprocess.check_output("vmstat -s", shell=True).strip().decode()
    context['ram_size'] = psutil.virtual_memory().total/1024/1024/1024
    context['ram_status'] = psutil.virtual_memory()
    return 0


def main():
    os_information()
    cpu()
    memory_information()
    return context


main()
