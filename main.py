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
    context['cpu_avg'] = os.getloadavg()
    print(context['cpu_avg'])
    context['cpu_information'] = subprocess.check_output("lscpu", shell=True).strip().decode()
    return context


def memory_information():
    context = {}
    context['memory'] = subprocess.check_output("vmstat -s", shell=True).strip().decode()
    context['ram_size'] = psutil.virtual_memory().total / 1024 / 1024 / 1024
    context['ram_status'] = psutil.virtual_memory()
    print(context['ram_status'])
    return context


def main():
    context = {}
    context.update(os_information())
    context.update(cpu())
    context.update(memory_information())
    response = requests.post('https://stage.htop.ir', data=context)
    print(response)


main()
