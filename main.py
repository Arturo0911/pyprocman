#!/usr/bin/python3

from time import sleep
from typing import Any
import sys
import signal
import psutil
from pprint import pprint

# def print_table(data):
#     col_widths = [15, 15]
#     headers = ["PID", "NAME"]

#     print(f"*"+"-"*sum(col_widths)+" ")
#     print("* {:{widths[0]}} | {:{widths[1]}}".format(headers[0],
#                                                      headers[1], widths=col_widths))
#     print("*" + "-" * sum(col_widths) + " ")
    
#     for row in data:
#             print("* {:{widths[0]}} | {:{widths[1]}}".format(row[0], row[1], widths=col_widths))
#             sleep(0.5)

# def printing_process(process: Any) -> None:

#     print(f"*    {process.pid}  {process.name()}")


def sig_handler(sig, frame):
    print("""\n\n\t[*] Exiting...\n\n""")
    sys.exit(0)


signal.signal(signal.SIGINT, sig_handler)


def main():
    try:
        # print_table()
        data = []
        process_info_list = []
        
        # list_table = [[x.info['pid'], x.info['name'], x.info['username'], x.info['memory_info'].rss / (1024 * 1024)] for x in psutil.process_iter(["pid", "name", "username", "memory_info"])]
        list_table = [[x.info['pid'], x.info['name'], x.info['username'], x.info['cpu_percent']] for x in psutil.process_iter(["pid", "name", "username", "cpu_percent"])]
        # # pprint(list_table)
        # for process in psutil.process_iter(['pid', 'name', 'username', 'memory_info', 'cpu_percent', 'status', 'create_time']):
        #     try:
        #         process_info = {
        #             'pid': process.info['pid'],
        #             'name': process.info['name'],
        #             'user': process.info['username'],
        #             'memory': process.info['memory_info'].rss / (1024 * 1024),  # in MB
        #             'cpu_percent': process.info['cpu_percent'],
        #             'status': process.info['status'],
        #             'create_time': process.info['create_time']
        #         }
        #         process_info_list.append(process_info)
        #     except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        #         pass
        
        
        for process in psutil.process_iter(["pid", "name", "username", "cpu_percent"]):
            try:
                process_info = {
                    "pid":process.info['pid'], 
                    "username":process.info['username']
                }
            except Exception as e:
                print(str(e))
        pprint(process_info)
    except Exception as e:
        print("Error by: ", str(e))
        sys.exit(1)


if __name__ == "__main__":
    main()
