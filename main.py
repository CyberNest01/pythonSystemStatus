import os
import subprocess
import psutil
import requests


def os_information():
    context = {}
    context['host_name'] = subprocess.check_output("hostname -I", shell=True).strip().decode()
    context['linux'] = subprocess.check_output("uname -v", shell=True).strip().decode().split('~')[1]
    context['uptime'] = subprocess.check_output("uptime", shell=True).strip().decode()
    context['kernel'] = subprocess.check_output("uname -r", shell=True).strip().decode()
    context['bash_version'] = subprocess.check_output("bash --version", shell=True).strip().decode().split('\nCopyright')[0]
    return context


def cpu():
    context = {}
    context['cpu_avg_1min'] = os.getloadavg()[0]
    context['cpu_avg_5min'] = os.getloadavg()[1]
    context['cpu_avg_15min'] = os.getloadavg()[2]
    context['cpu_information'] = subprocess.check_output("lscpu", shell=True).strip().decode()
    return context


def memory_information():
    context = {}
    context['memory'] = subprocess.check_output("vmstat -s", shell=True).strip().decode()
    context['ram_size'] = psutil.virtual_memory().total / 1024 / 1024 / 1024
    return context


def main():
    context = {}
    context.update(os_information())
    context.update(cpu())
    context.update(memory_information())
    context.update(ram_status_clear())
    response = requests.post('https://stage.htop.ir/', data=context)
    print(response)


def ram_status_clear():
    context = {}
    status = psutil.virtual_memory()
    context['ram_status_total'] = status[0]
    context['ram_status_available'] = status[1]
    context['ram_status_percent'] = status[2]
    context['ram_status_used'] = status[3]
    context['ram_status_free'] = status[4]
    context['ram_status_active'] = status[5]
    context['ram_status_inactive'] = status[6]
    context['ram_status_buffers'] = status[7]
    context['ram_status_cached'] = status[8]
    context['ram_status_shared'] = status[9]
    context['ram_status_slab'] = status[10]
    return context


main()
