import subprocess
import sys

def check_installed():
    try:
        import pip
        print("Pip is installed")
    except ImportError:
        print("Pip not present. Trying to install...")
        try:
            subprocess.check_call(['python3', 'get-pip.py'])
        except:
            sys.exit("Cannot install Pip... Exiting")

def install(name):
    try:
        subprocess.check_call(['pip3', 'install', name])
    except:
        print("Dependency couldn't be installed. Trying to continue execution...")