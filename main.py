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
    """
    x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]

    x.add_row(["Adelaide", 1295, 1158259, 600.5])
    x.add_row(["Brisbane", 5905, 1857594, 1146.4])
    x.add_row(["Darwin", 112, 120900, 1714.7])
    x.add_row(["Hobart", 1357, 205556, 619.5])
    x.add_row(["Sydney", 2058, 4336374, 1214.8])
    x.add_row(["Melbourne", 1566, 3806092, 646.9])
    x.add_row(["Perth", 5386, 1554769, 869.4])

    print(x)
    """

    x.field_names = ["username", "pid", "name", "cpu_percent", "memory_info"]
    for process in psutil.process_iter(["username", "pid", "name", "cpu_percent", "memory_info"]):
        # print(f"name: {x.info['name']}")
        # x.add_row([x.info["pid"], x.info["name"], x.info["username"]])
        x.add_row([process.info['username'], process.info['pid'], process.info['name'], f"{process.info['cpu_percent']} %", int(process.info['memory_info'].rss/(1024*1024))])
        


    print(x)


if __name__ == "__main__":
    main()
