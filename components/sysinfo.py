import sys
import platform

def get_system():
    return platform.system()

def get_cpuarchitecture():
    return platform.machine()