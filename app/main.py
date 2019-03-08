#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import argparse
import sys
import os

from cli import Client


def main():
    kwargs = {}
    platform = sys.platform
    kwargs["platform"] = platform

    if args.path:
        if os.path.isdir(args.path):
            kwargs["path"] = args.path
        else:
            raise NotADirectoryError("Target path is not directory")

    else:
        if platform == "linux":
            kwargs["path"] = "/home/"
        elif "win" in platform:
            kwargs["path"] = "C:"
    print(kwargs["path"])
    if args.output:
        if os.path.isdir(args.output):
            kwargs["output"] = args.output
        else:
            raise NotADirectoryError("Target output path is not directory")
    else:
        kwargs["output"] = ""

    if args.graphics:
        pass
        # Starts graphics session.
    else:
        client = Client(kwargs["platform"], kwargs["path"], kwargs["output"])
        client.backup()
        # Runs only CLI


parser = argparse.ArgumentParser(description="Backup client application",
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-g' '--graphics', dest='graphics', action='store_true',
                    help='Enables GUI')
parser.add_argument('--no-graphics', dest='graphics', action='store_false',
                    help='Disables GUI')
parser.set_defaults(graphics=False)
parser.add_argument('-p', '--path', action='store',
                    help='Path to directory for backup')
parser.add_argument('-o', '--output', action='store',
                    help='Path where the backup will be stored')
parser.add_argument('-r', '--restore', action='store_true',
                    help='Restores backup from target path to output')
args = parser.parse_args()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        pass
