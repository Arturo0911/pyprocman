#!/usr/bin/env python

import sys
import signal
import psutil
from pprint import pprint
from prettytable import PrettyTable


class ProcessEnumeration:
    def __init__(self):
        pass


def sig_handler():
    print("""\n\n\t[*] Exiting...\n\n""")
    sys.exit(0)


signal.signal(signal.SIGINT, sig_handler)


def main_():
    try:
        process_info = dict()
        data = list()
        for process in psutil.process_iter(["pid", "name", "username", "cpu_percent", "memory_info"]):
            try:
                process_info = {
                    "pid": process.info['pid'],
                    "username": process.info['username'],
                    "cpu_percent":process.info['cpu_percent'],
                    "memory_info":int(process.info['memory_info'].rss)/(1024 * 1024)
                }
                data.append(process_info)
            except Exception as e:
                print(str(e))
        pprint(data)
    except Exception as e:
        print("Error by: ", str(e))
        sys.exit(1)


def main():
    x = PrettyTable()
    x.field_names = ["username", "pid", "name", "cpu_percent", "memory_info"]
    for process in psutil.process_iter(["username", "pid", "name", "cpu_percent", "memory_info"]):
        # print(f"name: {x.info['name']}")
        # x.add_row([x.info["pid"], x.info["name"], x.info["username"]])
        x.add_row([process.info['username'], process.info['pid'], process.info['name'], f"{process.info['cpu_percent']} %", int(process.info['memory_info'].rss/(1024*1024))])
        


    print(x)


if __name__ == "__main__":
    main()
