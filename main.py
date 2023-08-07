#!/usr/bin/python3

from time import sleep
from typing import Any
import sys
import signal
import psutil


def printing_process(process: Any) -> None:
    print(f"[*] Priting PID: {process.pid} {process.name()}")


def sig_handler(sig, frame):
    print("""\n\n\t[*] Exiting...\n\n""")
    sys.exit(0)

signal.signal(signal.SIGINT, sig_handler)




def main():
    try:
        for process in psutil.process_iter(["pid", "name"]):
            printing_process(process)
            sleep(2)
    except Exception as e:
        print(str(e))
        sys.exit(1)    



if __name__ == "__main__":
    main()
