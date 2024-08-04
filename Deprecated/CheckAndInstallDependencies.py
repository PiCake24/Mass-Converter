import subprocess
import sys


def check_pip():
    try:
        result = subprocess.run(['pip', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        print("pip is installed.")
        return True
    except subprocess.CalledProcessError:
        print("pip is not installed.")
        return False


def install_pip():
    try:
        subprocess.check_call([sys.executable, '-m', 'ensurepip', '--upgrade', '--default-pip'])
        print("pip installed successfully.")
    except subprocess.CalledProcessError as e:
        print("Failed to install pip:", e)


def check_ctdb():
    try:
        import cdtb
        print("cdtb is installed.")
        return True
    except ImportError:
        print("cdtb is not installed.")
        return False


def install_cdtb():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'cdtb'])
        print(f"Successfully installed cdtb.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install cdtb: {e}")


def install_dependencies():
    if not check_ctdb():
        if not check_pip():
            install_pip()
        install_cdtb()