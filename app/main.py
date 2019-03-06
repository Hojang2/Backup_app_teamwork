#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import argparse
import sys
import os

parser = argparse.ArgumentParser(description="Backup client application",
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-g' '--graphics', dest='graphics', action='store_true',
                    help='Enables GUI')
parser.add_argument('--no-graphics', dest='graphics', action='store_false',
                    help='Disables GUI')
parser.set_defaults(graphics=False)
parser.add_argument('-p' '--path', action='store',
                    help='Path to directory for backup')
args = parser.parse_args()


def main():
    kwargs = {}

    if args.path:
        if os.path.isdir(args.path):
            kwargs["path"] = args.path
        else:
            raise NotADirectoryError("Target path is not directory")

    else:
        if sys.platform == "linux":
            kwargs["path"] = "/home/"
        elif sys.platform.startswith('win'):
            kwargs["path"] = "C:"

    if args.graphics:
        pass
        # Starts graphics session.
    else:
        pass
        # Runs only CLI


if __name__ == "__main__":
    main()
